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

s = sys.argv[1]
#print(f"https://mycima.nl/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-{sys.argv[1]}-%d9%85%d8%aa%d8%b1%d8%ac%d9%85-2/")
#getfilm(f"https://mycima.nl/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-{sys.argv[1]}-%d9%85%d8%aa%d8%b1%d8%ac%d9%85-2/")
getfilm(str(s))
