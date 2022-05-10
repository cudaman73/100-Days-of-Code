from bs4 import BeautifulSoup
import requests
from config import SPOTIFY_ID, SPOTIFY_SECRET
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

date = input("When do you want to travel to? Enter a date (YYYY-MM-DD):")
year = date[:4]
song_uris = []

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, 'html.parser')

chart = soup.find('div', class_='chart-results')
song_titles = [x.text.replace('\n', '').replace('\t', '') for x in chart.find_all('h3', class_='a-no-trucate')]

scope = 'user-read-private, playlist-modify-private'
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET,
                                                             scope=scope))
user_id = sp.current_user()["id"]

'''TODO: update song search algorithm to get songs more accurately. only grabs first song result, doesn't do any 
checking to see if it's correct or not '''
for song in song_titles:
    result = sp.search(q=f'track: {song} year: {year}', type='track')
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f'{song} has no search results in Spotify, so we\'re skipping')

playlist_id = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)['uri'].split(":")[2]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
