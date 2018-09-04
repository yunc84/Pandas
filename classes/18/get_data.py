import json
import requests
import sqlite3
import argparse

URL_BASE = 'https://api.spotify.com/v1/'
DATABASE_NAME = 'spotify.db'

def fetch_album_songs(album_id):

    url = URL_BASE + 'albums/' + album_id + '/tracks'  # 1

    response = requests.get(url)  # 2

    json_response = json.loads(response.text)  # 3

    songs = []

    for item in json_response['items']:  # 4

        track_num = item['track_number']
        name = item['name']
        duration = item['duration_ms']

        songs.append((track_num, name, duration))

    return songs  # 5


def store_in_database(songs):
    
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.executemany("""INSERT OR IGNORE INTO sgt_pepp_songs VALUES(?,?,?)""", songs)

    connection.commit()

    connection.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Specify an album id')
    parser.add_argument('-a', '--album_id', required=True, help='Spotify Album id')
    args = parser.parse_args()
    
    songs = fetch_album_songs(args.album_id)

    store_in_database(songs)
