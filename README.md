# Bandcamp genres twitter bot

Powering the following bots:

- Popular tags (400 or so, every 6 hours): **[@bc_pop_tags](https://twitter.com/bc_pop_tags)**
- Obscure genres (5000 or so, a few times a day): **[@bc_obscure_tags](https://twitter.com/bc_obscure_tags)**

## 🛠

- Python 3
- Requests
- Tweepy

## 🎧

The tags list is a file w/ one JSON object per line:

```
{ "value": "hip-hop-rap", "name": "hip-hop/rap" }
{ "value": "harsh-noise-wall", "name": "harsh noise wall" }
{ "value": "melodic-death-metal", "name": "melodic death metal" }
```

It's read in order (shuffle your lines beforehand if you want a random order)

## 🔥

### dev

using the default paths:

`python3 main.py`

using custom paths:

`python3 main.py -t ~/path_to/tab_list.txt -i ~/path_to/current_index.txt`

### prod

1. fill out `.secrets`:

```
export CONSUMER_KEY=…
export CONSUMER_SECRET=…
export ACCESS_TOKEN=…
export ACCESS_TOKEN_SECRET=…
```

2. run
`. .secrets && python3 main.py`

3. `crontab -e`

```
* */6 * * * cd ~/python-bandcamp-twitter-bot && . .secrets && python3 main.py -t ~/path_to/tab_list.txt -i ~/path_to/current_index.txt
```
