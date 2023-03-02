"""Example of Python client calling Knowledge Graph Search API."""

import json
from urllib.parse import urlencode
from urllib.request import urlopen
from pathlib import Path
from pprint import pprint

api_key = open(str(Path.home()) + "/.google_api_key").read()

# use Google search API to get information about a named entity:

def get_entity_info(entity_name):
    service_url = "https://kgsearch.googleapis.com/v1/entities:search"
    params = {
        "query": entity_name,
        "limit": 1,
        "indent": True,
        "key": api_key,
    }
    url = service_url + "?" + urlencode(params)
    response = json.loads(urlopen(url).read())
    return response

if __name__ == "__main__":
    pprint(get_entity_info("Mark Louis Watson"))
