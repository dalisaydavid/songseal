# app/recommendations/views.py

from collections import defaultdict
from functools import partial

from flask import render_template, request, redirect, url_for, current_app

from . import recommendations
from app import spotify, youtube
from app import utils

MAX_VIDEO_TITLE_LENGTH = 42
MAX_VIDEO_COUNT_PER_PAGE = 27

@recommendations.route('/recommendations/<username>', methods=['GET', 'POST'])
def recommendations_for_user(username):
    spotify_client = spotify.SpotifyClient(client_id=current_app.config['SPOTIFY_CLIENT_ID'], client_secret=current_app.config['SPOTIFY_CLIENT_SECRET'])
    playlist_tracks = spotify_client.get_user_playlist_tracks(username=username)

    youtube_client = youtube.YoutubeClient(api_key=current_app.config['YOUTUBE_CLIENT_ID'])

    videos = []
    for playlist_track in playlist_tracks:
        track_name = playlist_track[0]
        artist_name = playlist_track[1]
        videos.extend(
            youtube_client.search(
                options={
                    'query': '{track_name} {artist_name} cover'.format(track_name=track_name, artist_name=artist_name),
                    'max_results': 5
                }, 
                kind='video', 
                order='relevance'
            )
        )

    videos = map(
        partial(
            utils.transform_value_in_tuple,
            index=0,
            transform_function=partial(utils.limit_string_length, l=MAX_VIDEO_TITLE_LENGTH)
        ),
        videos
    )

    return render_template("recommendations/index.html", title="Recommendations", username=username, videos=videos[:MAX_VIDEO_COUNT_PER_PAGE])
    
@recommendations.route('/recommendations', methods=['POST'])
def recommendations():
    """
    Render the homepage template on the /recommendations route
    """
    username = request.form.get('username', 'spotify')

    return redirect(url_for('recommendations.recommendations_for_user',username=username))