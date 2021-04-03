import os
import requests
from bs4 import BeautifulSoup
import sys 


def getfilm(url):
    links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a'):
        lin = link.get('href')
        if"live" in lin:
            links.append(lin)
    print(links)
    for link in links:
        if "1080" in link:
            print("download in 1080p : " + link)
        if "720" in link:
            print("download in 720p : " + link)
        if "480" in link:
            print("download in 480p : " + link)
        if "360" in link:
            print("download in 360p : " + link)


getfilm(sys.argv[1])
