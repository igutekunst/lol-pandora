lol-pandora
===========

"The Worlds S***tiest Pandora Client"

A proof of concept pandora client using the pithos client library.


Utilizes GPL code from the Pithos pandora client. 


Requirements
============
sox, or another command line tool that can play mp3s

Python 3. Python 2.7 wil not work. The pandora client doesn't support it, and it's more than a trivial change to add support for Python 2.7

Currently the play program from the sox package is the best.

`` apt-get install sox``
or 
`` pacman -S sox ``
or ???

To use, create file called login.txt with your Pandora email on the first line, and password on the second line.


If you want to use a different mp3 play command line tool, edit main.py.


Notes
=====

This is a proof of concept project. It has no error checking, ~ no features, and probably is barely useful. 



So far, sox works the best. Install the package sox, and then use the "play" command

Disclaimer
==========

This project is in no way affiliated with Pandora. 

Please support Pandora by purchasing Pandora One rather than leeching bandwidth and ignore ads. 
