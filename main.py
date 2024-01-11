#!/usr/bin/python3

#TODO:
# get observations
# get flight data
# website?

import sys
import pyinaturalist as inat
from pprint import pprint
import json
import os

loc = sys.argv[1]

pprint(sys.argv)
response = inat.places.get_places_autocomplete(loc)
results = response["results"]
for result in results:
    print(f"name: {result['display_name']} id: {result['id']}")

jsonname = f"{loc.strip().lower()}.json"

if os.path.exists(jsonname):
  os.remove(jsonname)

f = open(jsonname, "w")
json.dump(result, f, indent=2)
f.close()