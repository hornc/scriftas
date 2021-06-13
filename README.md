# scriftas

Utility to produce SVG glyphs of Old Italic scripts, and similar.

For use in generating families of similar styled and scaled glyphs for representing Old Italic variant characters where regional variants and particular inscriptions of interest differ from what is available in Unicode.

Developed to fill in the gaps on Wikipedia's https://en.wikipedia.org/wiki/Old_Italic_scripts#Alphabets_related_to_Etruscan


Oscan _scriftas_ = Latin _scriptae_  (nom. pl.)

## About

Alphabets are composed of *glyphs*. *Glyphs* are composed of one or more *strokes*. *Strokes* are represented as tuples:

* **2-tuple:** Dot *(x₁, y₁)*
* **3-tuple:** Circle *(x₁, y₁, r)*
* **4-tuple:** Line (straight) *(x₁, y₁, x₂, y₂)*
* **6-tuple:** Curve *(x₁, y₁, x₂, y₂, c<sub>x</sub>, c<sub>y</sub>)*

The origin of each glyph *(0, 0)* is the top-left corner. The bottom-right corner is *(1, 1)*. The aspect ratio of the glyph is adjustable, and set by`height` and `width` in the alphabet.json file. `height = 180` and `width = 130` (pixels) is a sensible default.

The aim of this project/tool is to store just the abstract shape of a glyph as a set of tuples. Factors like stroke width, style, overall scale, orientation, skew, and aspect ratio can then be adjusted at the alphabet level. New alphabets can be generated (in SVG format) from the basic glyph shapes to serve different purposes.

The glyph data is stored in JSON format and processed to produce SVG output. The intent is that the JSON only stores the basic shape of the strokes, and a rendering engine can produde the final stroke in any way, whether it simulates engraving in clay or stone, produces neat SVGs with even width strokes, or converts to CNC G codes for actual engraving (not implemented here).

Single glyph example (Oscan P):

	{
		 "name": "P",
		 "transcription": "p",
		 "strokes": [[0.3, 0.2, 0.3, 1], [1, 0, 1, 1], [1, 0, 0.3, 0.2, 0.3, 0]]
	}
The full alphabet, with source reference, can be found in [alphabets/oscan.json](alphabets/oscan.json)

## Example Full Scripts
The following scripts are included in the distribution:
* [Etruscan](output/etruscan/README.md)
* [Etruscan (Archaic)](output/etruscanarchaic/README.md)
* [Oscan](output/oscan/README.md)
* [Umbrian](output/umbrian/README.md)

## Comments, Requests, and Contributions

Comments and suggestions are welcome, feel free to open an issue on this project's Github: https://github.com/hornc/scriftas

## Licenses
### Software
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[Scriftas](https://github.com/hornc/scriftas) - Utility to produce SVG glyphs of Old Italic scripts, and similar.

Copyright © 2020-2021 Charles Horn.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
[GNU General Public License](COPYING) for more details.

### Glyph source and output data
[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)

The glyph data files located in [alphabets/](alphabets/) in .json format, and the resulting SVG output is dedicated to the public domain under
[CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/deed.en)

The images in [output/](output/) also fall under the Wikimedia commons [Ancient scripts public domain declaration](https://commons.wikimedia.org/wiki/Template:PD-ancient-script):
> "[these images are] in the public domain because [they are] an SVG representaion of an ancient script."
