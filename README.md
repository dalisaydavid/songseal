# songseal 
[![Python Version](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/)

[![songseal](https://i.imgur.com/gBkDGBJ.jpg)](https://i.imgur.com/gBkDGBJ.jpg)

# Description
Minimalistic Flask app that checks for if any Youtube covers were made for songs found in your Spotify playlists.

# Installation

#### Setup Virtualenv
```
git clone git@github.com:dalisaydavid/songseal.git && cd songseal
```

```
pip install virtualenv
```

```
virtualenv --no-site-packages .venv
```

```
source .venv/bin/activate
```

```
pip install -r requirements.txt
```

#### Setup app configs and API keys
1. Add `instance/config.py` to `songseal` main directory.
2. Add the following config variables to that file: `SQLALCHEMY_DATABASE_URI` (postgres), `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `YOUTUBE_CLIENT_ID`. Obtain personal Spotify developer client id and secret from https://beta.developer.spotify.com/dashboard/login and youtube developer client from https://console.developers.google.com/. 
```python
# instance/config.py

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://USER:PASSWORD@localhost:5432/songseal'

SPOTIFY_CLIENT_ID = 'YOUR SPOTIFY API CLIENT ID'
SPOTIFY_CLIENT_SECRET = 'YOUR SPOTIFY API CLIENT SECRET'

YOUTUBE_CLIENT_ID = 'YOUR YOUTUBE API CLIENT ID'
```

## Running
```
source .venv/bin/activate
```

```
python run.py
```



