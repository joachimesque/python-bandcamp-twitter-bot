#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import time
import argparse

import bandcamp
import sentences
import files_handler
import twitter_utils

def get_content(args, current_index):
  # Get current index and tag

  file_contents = files_handler.get_tag_line(index_path = args.index_path,
                                             tag_list_path = args.tag_list_path,
                                             current_index = current_index)

  # Get album info from tag

  all_albums = bandcamp.get_albums_from_tag(tag = file_contents["tag"]['value'])
  album = all_albums['items'][0]

  return({ 'tag_name': file_contents["tag"]["name"],
           'title': album["title"],
           'artist': album["artist"],
           'album_url': album["tralbum_url"],
           'current_index': file_contents["current_index"],
           'should_retry': all_albums["discover_spec"]["spec_name"] == "all"})

def main():
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

  # Call function to retrieve content, retry if it should

  current_index = 0

  while True:
    content = get_content(args, current_index)
    current_index = content["current_index"]

    if content["should_retry"] == True:
      time.sleep(30)
      current_index += 1
    else:
      break

  # Get sentence

  sentence = sentences.get_sentence(tag_name = content['tag_name'],
                                    album_title = content['title'],
                                    album_artist = content['artist'],
                                    album_url = content['album_url'])

  # Output sentence

  twitter_utils.tweet(sentence)

  # Write new index

  files_handler.write_index(index= current_index,
                            index_path = args.index_path)


if __name__ == "__main__":
  main()