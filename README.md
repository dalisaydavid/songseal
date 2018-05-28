# songseal 
[![Python Version](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/)

[![songseal](https://i.imgur.com/gBkDGBJ.jpg)](https://i.imgur.com/gBkDGBJ.jpg)

# Description
Minimalistic Flask app that checks for if any Youtube covers were made for songs found in your Spotify playlists.

#### Setup app configs and API keys
1. Add `instance/config.py` to `songseal` main directory.
2. Add the following config variables to `instance/config.py`:
```python
# instance/config.py
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://USER:PASSWORD@localhost:5432/songseal'
SPOTIFY_CLIENT_ID = 'YOUR SPOTIFY API CLIENT ID'
SPOTIFY_CLIENT_SECRET = 'YOUR SPOTIFY API CLIENT SECRET'
YOUTUBE_CLIENT_ID = 'YOUR YOUTUBE API CLIENT KEY'
```
Note: You can obtain a personal Spotify developer client id and a secret from https://beta.developer.spotify.com/dashboard/login. You can obtain a Youtube developer client key from https://console.developers.google.com/. 

## Installation and running
We use Strap conventions to speed up and standardize environment setup. For more info, see https://github.com/github/scripts-to-rule-them-all.

#### Quick start the app
```bash
sh scripts/server
```

#### All available commands
```bash
sh scripts/bootstrap # Resolve all dependencies that the application requires to run.
sh scripts/setup     # Set up application for the first time after cloning, or set it back to the initial first unused state.
sh scripts/update    # Update application to run for its current state.
sh scripts/test      # IN PROGRESS - Test suite for the application.
sh scripts/server    # Launch the application and any extra required processes locally.
sh scripts/console   # IN PROGRESS - Launch a console for the application.
```