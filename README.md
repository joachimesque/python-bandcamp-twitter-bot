# Bandcamp genres twitter bot

Powering the following bots:

- Popular tags (400 or so, every 6 hours): https://twitter.com/bc_pop_tags
- Obscure genres (TBC)

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

`python3 main.py`

### prod

1. fill out `.secrets`:

```
export CONSUMER_KEY=…
export CONSUMER_SECRET=…
export ACCESS_TOKEN=…
export ACCESS_TOKEN_SECRET=…
```

2. run
`source .secrets && python3 main.py`

3. `crontab -e`

```
* */6 * * * cd ~/python-bandcamp-twitter-bot && source .secrets && python3 main.py
```
