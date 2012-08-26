whereonearth-country
==

The short version
--

Where On Earth (WOE) data for countries smushed up with Natural Earth (NE) 1:10m
data for countries. That's fancy talk for "polygons".

The longer version
--

It's still a bit of a moving target, specifically formatting and normalizing ket
names in the `properties` hash. For example, all the NE property keys are
prefixed with `ne:`. Most but not all the records have NE geometries associated
with them.

Things like the ["Hong Kong Special Administrative Region"](https://github.com/straup/whereonearth-country/blob/master/data/248/656/98/24865698.json)
which ... uh ... uh, well yeah. This is why we still have wars and stuff, isn't
it? Those are the kinds of fiddly details that still need to be worked out.

Suggestions and gentle cluebats are absolutely welcome.

Where possible corresponding Wikipedia page IDs have been added. I'd also really
like to include Geonames IDs since that would be both easy and useful. Please
for to be sending me a pull request if you've already got that data at hand.

The long version
--

_Forking GeoPlanet one place type a time._

This is an active but still experimental project to create a community-driven
project to maintain and update the Creative Commons licensed GeoPlanet dataset.

Rather than create a single repository with every record the plan is to create
smaller datasets organized by placetype in the hopes that they will be more
manageable to download and to update by users interested in particular place types.

Each location (country) is stored as a separate GeoJSON file. GeoJSON was
chosen because it has wide support in variety of GIS tools, most programming
languages (and specifically JavaScript), can be edited using any old text editor
(or Github's own "edit this page" functionality) and allows for any number of
custom key/value pairs using the GeoJSON _properties_ dictionary.

The naming convention for records is the country's Where On Earth (WOE) ID
followed by a ".json" extension. Records are stored in nested directories that
correspond to their WOE ID. The top level directory would be the first three
digits of a WOE ID, the second level directory would be the following three
digits (four through six) and so on until their are no more digits in the WOE
ID.

This repository includes countries from GeoPlanet (versions 7.3 through 7.6) as
compiled by [woedb](http://woe.spum.org). Where possible records have already
been updated to include corresponding concordances, for example Wikipedia or
Geonames IDs.

Each record contains a bounding box or a complex polygon defining the contour of
the country. Polygons are sourced from the August 2012 release of the [Natural
Earth 1:10m country boundaries](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/).

A word about Github
--

In the long-run Github may not be the best venue for managing all of these
records. But it's not an entirely crazy idea either so we're going to try it for
a while because it's easy and safe.

To do
--

* Merge and update records from the GeoPlanet 7.10 release.

Other WOE repositories
--

* [whereonearth-timezone](https://github.com/straup/whereonearth-timezone)

* [whereonearth-state](https://github.com/straup/whereonearth-state)

* [whereonearth-airport](https://github.com/straup/whereonearth-airport)

* [whereonearth-building](https://github.com/straup/whereonearth-building)

See also
--

* [Yahoo! GeoPlanet Data](http://developer.yahoo.com/geo/geoplanet/data/)

* [Natural Earth 1:10m Cultural Vectors](http://www.naturalearthdata.com/downloads/10m-cultural-vectors/)

* [Geonames](http://www.geonames.org/)

* [Wikipedia](http://www.wikipedia.org/)

* [Show Me the GeoJSON](http://straup.github.com/showme-the-geojson/)
