python-name-badge-creator
=========================

A simple set of python scripts for creating name tags based on a SVG template and a XSLX spreadsheet.
In fact, this is pretty much a hack once created for a larger meeting of German Scout Association of Saint George (DPSG). Hence, the functionality is limited, and there are still some awkward German strings around.

For using this stuff, you'll need to do the following:

- Prepare a XLSX file with the people you want to create badges for
- Create an SVG template for the badge design. It uses two markers that are presently replaced with the firstname and the persons' job description (for example Troop Leader). If you need to add more fields, adapting the Python code  should be pretty much straight forward.
- Configure badge.conf accordingly. Here you'll also find settings for mapping spreadsheet cells to the Markers
- Once done, fire up makeBadges.py and you should be all set.

A second script, makePDFs.py, parses the configuration and launches Inkscape for a batch conversion of all name tags to PDF.

This is pretty limited. Pull requests welcome :D

