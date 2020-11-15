#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
import linecache
import sys

def get_tag_line(index_path, tag_list_path, current_index):
  if current_index == 0:
    current_index = linecache.getline(index_path, 1)

  try:
    current_index = int(current_index)
    tag_line = linecache.getline(tag_list_path, current_index).strip()

    if tag_line == '':
      raise ValueError()
  except:
    current_index = 1
    tag_line = linecache.getline(tag_list_path, 1).strip()

  try:
    tag_line = json.loads(tag_line)
  except:
    print("Error: there was a problem getting the tag line.")
    sys.exit()

  return {"current_index": current_index, "tag": tag_line}

def write_index(index, index_path):
  with open(index_path, 'w') as index_file:
    index_file.write(str(index + 1))

  index_file.close()
