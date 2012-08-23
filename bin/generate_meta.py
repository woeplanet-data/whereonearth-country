#!/usr/bin/env python

import sys
import json
import os
import csv

import utils

import logging
logging.basicConfig(level=logging.INFO)

countries = {}
iso_codes = {}

if __name__ == '__main__':

    whoami = os.path.abspath(sys.argv[0])
    bindir = os.path.dirname(whoami)
    rootdir = os.path.dirname(bindir)

    datadir = os.path.join(rootdir, 'data')
    metadir = os.path.join(rootdir, 'meta')

    # generate a list of all the countries - assume the extractotron cities.txt
    # https://github.com/migurski/Extractotron/blob/master/cities.txt

    countries_path = os.path.join(metadir, 'countries.tsv')
    countries_fh = open(countries_path, 'w')

    countries_writer = csv.writer(countries_fh, delimiter='\t')
    countries_writer.writerow(('top', 'left', 'bottom', 'right', 'slug', 'name', 'iso', 'woeid'))

    for root, dirs, files in os.walk(datadir):

        for f in files:

            path = os.path.join(root, f)
            logging.info("processing %s" % path)

            fh = open(path)
            data = json.load(fh)

            feature = data['features'][0]
            props = feature['properties']

            this_woeid = props['woe:id']
            this_country = None

            if not countries.get(this_country, False):
                countries[this_country] = []

            try:
                centroid = [ props['longitude'], props['latitude'] ]
            except Exception, e:
                logging.error("failed to process %s: %s" % (path, e))
                # wtf?
                continue

            add_country = True

            for pt in ('sw_latitude', 'sw_longitude', 'ne_latitude', 'ne_longitude'):
                if not props.get(pt, False):
                    add_country = False
                    break

            if add_country:

                countries_writer.writerow((
                        props['ne_latitude'],
                        props['sw_longitude'],
                        props['sw_latitude'],
                        props['ne_longitude'],
                        props['woe:id'],
                        props['name'].encode('utf-8'),
                        props['iso'],
                        props['woe:id']
                        ))

            iso_codes[props['woe:id']] = props['iso']

    countries_fh.close()

    # generate some basic stats (as a CVS file)

    csv_path = os.path.join(metadir, 'countries.csv')
    csv_fh = open(csv_path, 'w')

    writer = csv.writer(csv_fh)
    writer.writerow(('iso', 'woeid'))

    tmp = {}

    for k,v in iso_codes.items():
        tmp[v] = k

    codes = tmp.keys()
    codes.sort()

    for iso in codes:

        woeid = tmp[iso]

        logging.info("%s (%s)" % (iso, woeid))
        writer.writerow((iso, woeid))

    csv_fh.close()
