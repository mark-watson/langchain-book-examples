"""Example of Python client calling Knowledge Graph Search API."""

from pprint import pprint

import Google_KG_helper

if __name__ == "__main__":
    pprint(Google_KG_helper.get_entity_info("Mark Louis Watson"))
