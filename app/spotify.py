import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyClient:
    def __init__(self, client_id, client_secret):
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
        self.spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    def get(self):
        return self.spotify

    def get_user_playlist_tracks(self, username):
        playlists_response = self.spotify.user_playlists(username)
        playlist_tracks = []
        for playlist in playlists_response['items']:
            tracks_response = self.spotify.user_playlist(username, playlist['id'], fields="tracks,next")
            tracks = tracks_response['tracks']

            while True:
                track_names_and_artists = map(
                    lambda track_item: (
                        track_item['track']['name'].encode('ascii', 'ignore'),
                        track_item['track']['artists'][0]['name'].encode('ascii', 'ignore')
                    ),
                    tracks['items']
                )

                playlist_tracks.extend(track_names_and_artists)
                
                if tracks['next']:
                    tracks = self.spotify.next(tracks)
                else:
                    break

        return playlist_tracks


