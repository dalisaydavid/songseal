from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class YoutubeClient:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def search(self, options, kind='video', order='relevance'):
        search_response = self.youtube.search().list(
            q=options['query'],
            part='id,snippet',
            maxResults=options['max_results'],
            order=order
        ).execute()

        videos = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video' and kind == 'video':
                title = search_result['snippet']['title'].encode('ascii', 'ignore')
                video_id = search_result['id']['videoId'].encode('ascii', 'ignore')
                videos.append((title, video_id))

        return videos