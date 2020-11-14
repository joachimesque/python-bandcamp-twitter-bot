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
    "Right now, I need %s. And by that I mean %s, by %s",
    "%s. That’s it, that’s the tweet.\n\n%s\n%s",
    "Have you heard of %s? Ok, I thought so. But have you heard of %s, by %s?",
    "Today’s kids listen to %s all the time. And they prefer %s, by %s.",
    "Currently trending: #%s\n%s, by %s",
    "%s\n%s\n%s\nGo.\nListen.",
    "What would you listen if you were into %s? Easy answer, %s, by %s",
    "Yes, sex is good, but have you heard of %s?\n%s\n%s",
    "Look what I picked yesterday at the %s store, %s by %s",
    "I’ve got an illness, and the answer is more %s.\n%s\n%s",
  ]
  random_sentence = random.choice(sentences) + "\n\n%s"

  return random_sentence % (tag_name, album_title, album_artist, album_url)
