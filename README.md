# Spotify Playlist Creator

Create a playlist on Spotify and add all songs from another to it.

**NOTE**: Only the first 100 songs will be added to the playlist.

## Usage

```
src/main.py [action]

Actions:
	add		Add songs to an already existing spotify playlist.
	create		Add songs to a newly created spotify playlist.
```

### Examples:

```console
$ python src/main.py create
Enter the playlist id you want to scrape: 0OYk0cjGUZHyRI76qsaXZO?si=1eca610412094c88
Enter a playlist name: new playlist
Enter a playlist description: new playlist
Finding songs
Filling playlist
Creating playlist
Created playlist ID: 19qOuJY6iE5TXjThL0RlZk
```

```console
$ python src/main.py add
Enter the playlist id you want to scrape: 0VrTF4UIcSqmPSoPysoiMZ?si=e8a0aa5c53e644c9
Finding songs
Filling playlist
Enter the playlist id of the playlist to which you want to add the songs: 19qOuJY6iE5TXjThL0RlZk # Part before '?si=....'
```

## Example .env

```
TOKEN="YOUR TOKEN"
USER_ID="YOUR SPOTIFY ID"
```

To get a token you can visit the following [Spotify API documentation ](https://developer.spotify.com/console/post-playlists/)

