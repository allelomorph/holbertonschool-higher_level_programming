#!/usr/bin/python3
"""0x0B. Python - Input/Output, task 9. Load, add, save  """


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

argv_edit = argv[1:]

try:
    content_list = load_from_json_file("add_item.json")
except:
    content_list = []
finally:
    for arg in argv_edit:
        content_list.append(arg)
    save_to_json_file(content_list, "add_item.json")
