from pandora.pandora import Pandora
from pandora.data import *
import sys
import subprocess
import os, errno, re, unicodedata

MP3_PLAYER = 'play'

def main():

    tmp = "/tmp/lolpiano" 
    try:
        os.mkdir(tmp)
    except OSError as e:
        if e.errno == errno.EEXIST and os.path.isdir(tmp):
            pass
        else:
            raise e
    email = ""
    password = ""
    with open("login.txt", "r") as f:
        (email, password) = (l.rstrip() for l in f.readlines())

    pandora = Pandora()

    client = client_keys[default_one_client_id]

    pandora.connect(client, email, password)
    pandora.set_audio_quality("highQuality")

    for i, station in enumerate(pandora.stations):
        print (i, station.name)
    try:
        station = int (input("Enter a station number "))
    except ValueError:
        print ("invalid station number.Quitting.")
        sys.exit(1)

    station = pandora.stations[station]

   
    while True:
        songs = station.get_playlist()

        for song in songs: 
            filename = '{0} - {1} - {2}.mp3'.format(song.artist, song.album, song.songName)


            filename = os.path.join('/tmp/lolpiano/', filename)
            url = song.audioUrl
            subprocess.call(['wget', 
                             url, 
                             '--output-document',
                             filename
                            ])
            print ( 'Playing {0}'.format(song.title))

            subprocess.call([MP3_PLAYER,
                              filename
                            ])




if __name__ =='__main__':
  main()
