# scriftas

Utility to produce SVG glyphs of Old Italic scripts, and similar.

For use in generating families of similar styled and scaled glyphs for representing Old Italic variant characters where regional variants and particular inscriptions of interest differ from what is available in Unicode.

Developed to fill in the gaps on Wikipedia's https://en.wikipedia.org/wiki/Old_Italic_scripts#Alphabets_related_to_Etruscan

My Wikipedia user sandbox with current progress: https://en.wikipedia.org/wiki/User:Salpynx/sandbox#From_Old_Italic_scripts 


Oscan _scriftas_ = Latin _scriptae_  (nom. pl.)

## About

Alphabets are composed of *glyphs*. *Glyphs* are composed of one or more *strokes*. *Strokes* are represented as tuples:

* **2-tuple:** Dot *(x₁, y₁)*
* **3-tuple:** Circle *(x₁, y₁, r)*
* **4-tuple:** Line (straight) *(x₁, y₁, x₂, y₂)*
* **6-tuple:** Curve *(x₁, y₁, x₂, y₂, c<sub>x</sub>, c<sub>y</sub>)*

The origin of each glyph *(0, 0)* is the top-left corner. The bottom-right corner is *(1, 1)*. The aspect ratio of the glyph is adjustable, and set by`height` and `width` in the alphabet.json file. `height = 180` and `width = 130` (pixels) is a sensible default.

The aim of this project/tool is to store just the abstract shape of a glyph as a set of tuples. Factors like stroke width, style, overall scale, orientation, skew, and aspect ratio can then be adjusted at the alphabet level. New alphabets can be generated (in SVG format) from the basic glyph shapes to serve different purposes.

## License
Scriftas - Utility to produce SVG glyphs of Old Italic scripts, and similar.

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
The glyph data files located in [alphabets/](alphabets/) in .json format, and the resulting SVG output is dedicated to the public domain under
https://creativecommons.org/publicdomain/zero/1.0/deed.en
and https://commons.wikimedia.org/wiki/Template:PD-ancient-script
