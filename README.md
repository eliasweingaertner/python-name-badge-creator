python-name-badge-creator
=========================

A simple set of python scripts for creating name/tags badges based on a SVG template and a XSLX spreadsheet.
In fact, this is pretty much a hack creating once for a larger meeting of German Scouts (DPSG). Hence, the functionality is limited.

For using this stuff, you'll need to do the following:

- Prepare a XLSX file with the people you want to create badges for
- Create an SVG template for the badge design. It uses two markers #VORNAME# for Firstname and #FUNKTION# for the position of the person (for example Troop Leader).
- Configure badge.conf accordingly. Here you'll also find settings for mapping spreadsheet cells to the Markers

Once done, fire up makeBadges.py and you should be all set.

This is pretty limited. Pull requests welcome :D

