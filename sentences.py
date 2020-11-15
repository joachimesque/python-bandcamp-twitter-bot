#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import random

def get_sentence(tag_name, album_title, album_artist, album_url):
  sentences = [
    "Psst, I heard you like {tag}… I think you should listen to {album}, by {artist}.",
    "All the {tag}-heads should give an ear to {album} from {artist}.",
    "So I heard you loved {tag} music, so you have to hear {album} from {artist}.",
    "My scene is not usually {tag}, but I really enjoyed {album}, by {artist}.",
    "{tag}!! Yes!! Especially with {album}, by {artist}.",
    "Let’s discover something new today, perhaps in {tag}?  Here, {album}, by {artist}.",
    "Right now, I need {tag}. And by that I mean {album}, by {artist}.",
    "{tag}. That’s it, that’s the tweet.\n\n{album}\n{artist}",
    "Have you heard of {tag}? Ok, I thought so. But have you heard of {album}, by {artist}?",
    "Today’s kids listen to {tag} all the time. And they prefer {album}, by {artist}.",
    "Currently trending: #{tag}\n{album}, by {artist}.",
    "{tag}\n{album}\n{artist}\nGo.\nListen.",
    "What would you listen if you were into {tag}? Easy answer, {album}, by {artist}.",
    "Yes, sex is good, but have you heard of {tag}?\n{album}\n{artist}.",
    "Look what I picked yesterday at the {tag} store: {album} by {artist}.",
    "I’ve got an illness, and the answer is more {tag}.\n{album}\n{artist}",
    "{tag}. The new sound. Of course, it’s {album}, by {artist}.",
    "If you want to hear tomorrow’s {tag}, listen to {album}, by {artist}.",
    "You think you know {tag}? Wait until you hear {album}, from {artist}.",
    "Everything in {tag} has been done, so they say. Everything? No! {album} by {artist} ups the ante.",
    "I like {tag}, and {album}, by {artist}, is my new jam.",
    "np #{tag} 🎧\n{album}, {artist}\n🎶",
    "I’m a simple man, listening to simple {tag}. {album}, by {artist}? Thats what I like.",
    "All the real {tag} fans should get {album}, by {artist}. All the unreal ones too.",
    "In jazz they say Miles is still miles ahead, but in {tag}, it's {album}, by {artist}.",
    "Yes I like {tag}. Why do you ask, is it because I just put {album}, by {artist}?",
    "Hand me the AUX cord, I got the latest {artist} 🔥🔥🔥\n\n#{tag} #🔥🔥🔥 #🚒",
    "Time to try {tag}, starting with {album} by {artist}",
    "I need coffee and {tag}. So here’s {artist} with {album}.",
    "{tag} is coming back hard with {album} by {artist}",
    "{artist} is in town, bringing us {album}. #{tag}",
    "{artist}’s {album} has your daily dose of {tag}",
    "{artist} is what {tag} fans are into, so check out {album}",
    "I like big {tag} and I cannot lie. You other {artist} fans can’t deny.",
    "Simply #{tag}",
  ]
  random_sentence = random.choice(sentences) + "\n\n{album_url}"

  return random_sentence.format(
    tag = tag_name,
    album = album_title,
    artist = album_artist,
    album_url = album_url
  )
