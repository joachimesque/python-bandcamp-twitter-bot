#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import json
import requests

def get_albums_from_tag(tag):
  url = "https://bandcamp.com/api/hub/2/dig_deeper"
  headers = {
    'Content-Type': 'application/json'
  }

  request_dict = {'filters':{'format':'all','location':0,'sort':'pop','tags':[tag]},'page':1}
  payload = json.dumps(request_dict)
  response = requests.request("POST", url, headers = headers, data = payload)

  response_object = response.json()

  return(response_object)