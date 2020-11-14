#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import random

def get_sentence(tag_name, album_title, album_artist, album_url):
  sentences = [
    "Psst, I heard you like %s… I think you should listen to %s, by %s",
    "All the %s-heads should give an ear to %s from %s",
    "So I heard you loved %s music, so you have to hear %s from %s",
    "My scene is not usually %s, but I really enjoyed %s, by %s",
    "%s!! Yes!! Especially with %s, by %s",
    "Let’s discover something new today, perhaps in %s?  Here, %s, by %s",
  ]
  random_sentence = random.choice(sentences) + "\n\n%s"

  return random_sentence % (tag_name, album_title, album_artist, album_url)
