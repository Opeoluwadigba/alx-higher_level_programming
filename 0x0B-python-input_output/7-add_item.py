#!/usr/bin/python3
"""
Script that updates a list as a JSON representation.
"""



from sys import argv
save_json = _import_('5-save_to_json_file').save_to_json_file
load_json = _import_('6-load_fron_json_file').load_from_json_file

filename = "add_item.json"

try:
    list_arg = load_json(filename)
except:
    list_arg = []

with open(filename, 'w', encoding="utf-8")
     for arg in argv[1]:
         list_arg.append(arg)
         save_json(list_arg, filename)
