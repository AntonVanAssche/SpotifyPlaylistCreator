#!/usr/bin/env python3

import json
import requests
import os
import sys
from dotenv import load_dotenv

def usage():
    print(sys.argv[0] + " [action]")
    print()
    print("Actions:")
    print("\tadd\t\tAdd songs to an already existing spotify playlist.")
    print("\tcreate\t\tAdd songs to a newly created spotify playlist.")

# Retrieve a list of all songs in the specified playlist.
# Reference: https://developer.spotify.com/console/get-playlist-tracks/
def find_songs():
    print("Finding songs")

    # Spotify API call to retrieve playlist information.
	# This is needed so we can extract all songs.
    query = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
    response = requests.get(query,
                            headers={"Content-Type": "application/json",
                                     "Authorization": "Bearer " + token})

    response_json = response.json()

    # Check whether the response contains at least one song.
    # Error out when non is found.
    if "tracks" in response_json:
        songs = ""

        # Extract all songs from the JSON response
        # so we can create a songs URI for later use.
        for i in response_json["tracks"]["items"]:
            songs += (i["track"]["uri"] + ",")
        songs = songs[:-1]

        # Start filling the (new) playlist.
        fill_playlist(songs)
    else:
        print("Failed to retrieve songs")
        sys.exit(1)

# When the user specified `create` this function will create a playlist.
# Reference: https://developer.spotify.com/console/post-playlists/
def create_playlist():
    print("Creating playlist")

    # Spotify API call to create a new playlist.
    query = "https://api.spotify.com/v1/users/" + user_id + "/playlists"
    request_body = json.dumps({
        "name": new_playlist_name,
        "description": "Playlist created by a BOT! 🤪",
        "public": "true"
    })
    response = requests.post(query, data=request_body, headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    })

    response_json = response.json()

    print("Created playlist ID: " + response_json["id"])
    return response_json["id"]

# Fill the (created) playlist with the retrieved songs.
# Reference: https://developer.spotify.com/console/post-playlist-tracks/
def fill_playlist(songs=""):
    print("Filling playlist")

    if action == "create":
        created_playlist_id = create_playlist()

    if action == "add":
        created_playlist_id = input("Enter the playlist id of the playlist to which you want to add the songs: ")

    # Spotify API call to add songs to thelaylist.
    query = "https://api.spotify.com/v1/playlists/" + str(created_playlist_id) + "/tracks?uris=" + songs
    response = requests.post(query, headers={"Content-Type": "application/json",
                                             "Authorization": "Bearer "+ token})

# Main
if __name__ == "__main__":
    if len(sys.argv) - 1 != 1:
        print("Please specify an action as a argument: add or create")
        usage()
        sys.exit(1)

    # Read Environment Variables From Env File.
    load_dotenv()

    # Retrieve the users spotify user id and token from the .env file.
    user_id = os.getenv("USER_ID")
    token = os.getenv("TOKEN")

    # This can be either add or create.
    action = sys.argv[1]

    playlist_id = input("Enter the playlist id you want to scrape: ")

    if action == "create":
        new_playlist_name = input("Enter a playlist name: ")

    # Start scraping the playlist.
    find_songs()
