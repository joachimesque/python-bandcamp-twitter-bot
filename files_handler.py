#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
import linecache
import sys

def get_tag_line():
  current_index = linecache.getline('current_index.txt',1)

  try:
    current_index = int(current_index)
  except:
    current_index = 1

  tag_line = linecache.getline('tag_list.txt', current_index).strip()

  if tag_line == '':
    current_index = 1
    tag_line = linecache.getline('tag_list.txt', 1).strip()

  return [current_index, json.loads(tag_line)]

def write_index(current_index):
  with open('current_index.txt', 'w') as index_file:
    index_file.write(str(current_index + 1))

  index_file.close()
