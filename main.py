#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import files_handler
import bandcamp
import sentences
import twitter_utils

file_contents = files_handler.get_tag_line()
current_index = file_contents[0]
tag = file_contents[1]
tag_value = tag['value']
tag_name = tag['name']

all_albums = bandcamp.get_albums_from_tag(tag = tag_value)

album = all_albums['items'][0]
album_title = album['title']
album_artist = album['artist']
album_url = album['tralbum_url']

sentence = sentences.get_sentence(tag_name, album_title, album_artist, album_url)

twitter_utils.tweet(sentence)

files_handler.write_index(current_index)
