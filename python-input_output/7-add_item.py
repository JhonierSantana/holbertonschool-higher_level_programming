#!/usr/bin/python3
"""
    Script to save arguments to a file
"""

import sys
import json
from typing import List
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
    items = []

items += sys.argv[1:]

save_to_json_file(items, "add_item.json")
