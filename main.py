#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import files_handler
import bandcamp
import sentences
import twitter_utils
import argparse

# Parse arguments

parser = argparse.ArgumentParser("Bandcamp Twitter tool")
parser.add_argument("-i", "--index_path",
                    help="Path to your index file",
                    default="./current_index.txt",
                    nargs="?",
                    type=str
                    )
parser.add_argument("-t", "--tag_list_path",
                    help="Path to your tag list file",
                    default="./tag_list.txt",
                    nargs="?",
                    type=str
                    )
args = parser.parse_args()
index_path = args.index_path
tag_list_path = args.tag_list_path

# Get current index and tag

file_contents = files_handler.get_tag_line(index_path = index_path,
                                           tag_list_path = tag_list_path)
current_index = file_contents[0]
tag = file_contents[1]
tag_value = tag['value']
tag_name = tag['name']

# Get album info from tag

all_albums = bandcamp.get_albums_from_tag(tag = tag_value)
album = all_albums['items'][0]

# Get sentence

sentence = sentences.get_sentence(tag_name = tag_name,
                                  album_title = album['title'],
                                  album_artist = album['artist'],
                                  album_url = album['tralbum_url'])

# Output sentence

twitter_utils.tweet(sentence)

# Write new index

files_handler.write_index(index= current_index,
                          index_path = index_path)
