#!/usr/bin/env python3
import argparse
import json
import sys

"""
    Scriftas.
    Utility to produce SVG glyphs of Old Italic scripts, and similar.
"""

__version__ = '0.5.0'


body = f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.0//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<!-- This SVG glyph was created with Scriftas v{__version__} (https://github.com/hornc/scriftas) and is licensed under a %%LICENSE%% license. -->
<svg xmlns="http://www.w3.org/2000/svg"
   version="1.0"
   id="%%NAME%%"
   x="0px"
   y="0px"
   width="%%WIDTH%%"
   height="%%HEIGHT%%"
>
%%CONTENT%%
</svg>
"""


# Summary output style
STYLE = """
    img {width: 44px;}
    td {text-align: center;}
    td.incomplete {background-color: #fdd;}
"""


def line(strokes, h, w, s):
    h -= 2 * s
    w -= 2 * s
    stroke_width = s * 2 / 3 if len(strokes) == 2 else s
    style = 'fill="none" stroke="#000" stroke-width="%d" stroke-linecap="round" stroke-linejoin="round"' % stroke_width
    if len(strokes) == 4:
        x1, y1, x2, y2 = strokes
        line = '<line %s ' % style
        line += 'x1="%s" y1="%s" x2="%s" y2="%s" />' % (x1 * w + s, y1 * h + s, x2 * w + s, y2 * h + s)
    elif len(strokes) in (2, 3):
        # dot / circle
        cx, cy = strokes[:2]
        if len(strokes) == 3:
            r = strokes[2] * (min(w, h) + s) / 2
        else:
            r = s / 3
        cx = cx * w + s
        cy = cy * h + s
        line = '<circle %s ' % style
        line += 'cx="%s" cy="%s" r="%s" />' % (cx, cy, r)
    elif len(strokes) == 6:
        x1, y1, x2, y2, cx, cy = strokes
        x1 = x1 * w + s
        y1 = y1 * h + s
        x2 = x2 * w + s - x1
        y2 = y2 * h + s - y1
        cx = cx * w + s - x1
        cy = cy * h + s - y1
        line = '<path %s ' % style
        line += 'd="M %s %s q %s %s %s %s" />' % (x1, y1, cx, cy, x2, y2,)
    return line


def letter_name(script, letter, variant=1):
    return '%s%s-%02d' % (script, letter, variant)


def fname(script, letter, variant=1):
    return letter_name(script, letter, variant) + '.svg'


def output_markdown(json):
    glyphs = ''.join(['![%s](./%s) ' % (a['name'], fname(json['name'], a['name'], a.get('variant', 1))) for a in json['letters']])
    body = f"""# {json['name']}
The SVG glyphs in this directory are licensed under a {json['license']} license.

{glyphs}

**Source:** [{json['sources'][0]}]({json['sources'][1]})"""
    return body

def output_summary(json):
    glyphs = ''.join(['<td class="%s"><img src="%s"></td>' % ('incomplete' if a.get('incomplete') else 'glyph', fname(json['name'], a['name'], a.get('variant', 1))) for a in json['letters']]) 
    transcription = ''.join(['<td>%s</td>' % a['transcription'] for a in json['letters']]) 
    body = """<html><head><title>{name} Glyphs</title><style>{style}</style></head><body>
    <h1>{name}</h1>
    <div>Source: <a href="{url}">{bib}</a></div>
    <table>
      <tr>{glyphs}</tr>
      <tr>{transcription}</tr>
    </table></body></html>
""".format(name=json['name'],
           glyphs=glyphs,
           transcription=transcription,
           url=json['sources'][1],
           bib=json['sources'][0],
           style=STYLE)
    return body


if __name__ == '__main__':
    """
    Parse input and produce output files
    """
    parser = argparse.ArgumentParser(description=f'Scriftas v{__version__}.')
    parser.add_argument('infile', help='JSON format alphabet file')
    parser.add_argument('-o', '--output', help='Output directory path to write SVG glyphs', default=".")
    args = parser.parse_args()

    with open(args.infile, 'r') as f:
        data = json.loads(f.read())

    w = data.get('width', 130)
    h = data.get('height', 180)
    stroke_width = round(min(w, h)**0.55)

    for letter in data.get('letters'): 
        name = letter_name(data['name'], letter['name'], letter.get('variant', 1))
        outfile = f'{args.output}/{name}.svg'
        output = body.replace('%%NAME%%', name)
        strokes = [line(st, h, w, stroke_width) for st in letter['strokes']]
        output = output.replace('%%CONTENT%%', ''.join(strokes)).replace('%%WIDTH%%', str(w)).replace('%%HEIGHT%%', str(h)).replace('%%LICENSE%%', data.get('license', 'UNKNOWN'))
        with open(outfile, 'w') as f:
            f.write(output)

    # Write HTML and markdown summary files
    with open(f'{args.output}/index.html', 'w') as index:
        index.write(output_summary(data))
    with open(f'{args.output}/README.md', 'w') as md:
        md.write(output_markdown(data))

