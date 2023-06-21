# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:02:58 2023

@author: AQ
"""
# import YouTube from pytube library 
# import argv from sys to pass command line arguments
from pytube import YouTube
from sys import argv

# get link and destinaitn path passed by user in command line arguments
link = argv[1]
dest = argv[2]

# pass link to Youtube method
yt = YouTube(link)

#donload video from youtube at highest availablle resolution
yd = yt.streams.get_highest_resolution()

#Save downloaded video at desired path
yd.download(dest)
