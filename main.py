from ast import If
from doctest import OutputChecker
from fileinput import filename
import imp
from msilib.schema import Directory
import sys
import socket
import subprocess
import os
import time
import signal
import random
import string
import threading
import re
from unittest import result
from urllib import request
from pytube.__main__ import YouTube
from tokenize import Number
from turtle import title

def print_banner():
    banner = """
  _____   __  ____   ____  ____  ______    ___  ____  
 / ___/  /  ]|    \ l    j|    \|      T  /  _]|    \ 
(   \_  /  / |  D  ) |  T |  o  )      | /  [_ |  D  )
 \__  T/  /  |    /  |  | |   _/l_j  l_jY    _]|    / 
 /  \ /   \_ |    \  |  | |  |    |  |  |   [_ |    \ 
 \    \     ||  .  Y j  l |  |    |  |  |     T|  .  Y
  \___j\____jl__j\_j|____jl__j    l__j  l_____jl__j\_j
"""
    print(banner) 

print_banner()

def url_creator():
    if not re.match(r'http(s?)\:', url):
        url = 'http://' + url
        parsed = urlsplit(url)
        host = parsed.netloc
        if host.startswith('www.'):
            host = host[4:]
        return host

def check_net():
    os.system('ping -c1 github.com > rs_net 2>&1')
    if "0% packet loss" in open ('rs_net').read():
        val = 1
    else:
        val = 0
    os.system('rm rs_net > /dev/null/ 2>&1')
    return val

def youtube_downloader():
    link = input("enter youtube link of video: ")
    yt = YouTube(link)
    
    print("title: ", yt.title)
    print("number of views: ",yt.views)
    print("length of video: ",yt.length)
    ys = yt.streams.get_highest_resolution()
    
    print("Downloading...")
    ys.download()
    print("Download completed")

def youtube_mp3():
    yt = YouTube(
        str(input("enter the url of the video you want to download: \n>> "))
    )
    video = yt.streams.filter(only_audio=True).first()
    print("video found")
    print("enter the destination")
    destination = str(input(">> ")) or '.'
    out_file = video.download(output_path=destination)
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    print(yt.title + "download completed!!")

def github_downloader():
    url = input("enter the link: ")
    directory = getcwd()
    filename = directory + 'somefile.txt'
    r = requests.get(url)
    f = open(filename, 'w')
    f.write(r.content)
    
def  vulner():
    intervals = (
        ('h', 3500),
        ('m', 60),
        ('s', 1),
    )
    def display_time(seconds, granularity=3):
        result[]
        seconds = seconds + 1
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                result.append("{}{}".format(value, name))
                return ' '.join(result[:granularity])
    def url_maker(url):
        if not re.match(r'http(s?)\\:')        


print("1)YouTube Video Downloader")
print("2)YouTube MP3 Downloader")
print("3)Github File Downloader")
print("4)Vulnerability Scanner")

opt = input("Select option: ")

if (opt=="1"):
    youtube_downloader()
    
elif( opt=="2"):
    youtube_mp3()
    
elif(opt =="3"):
    github_downloader()
    
elif (opt =="4"):
    vulner()
