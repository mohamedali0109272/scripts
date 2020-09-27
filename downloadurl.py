import os
import requests
from bs4 import BeautifulSoup

def getfilm(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('a' , class_="DownloadURL nobind Hoverable")['href']
    print(results)
    api =f"https://api.streamtape.com/remotedl/add?login=57d259db418ade6a4222&key=9ODPQYMXPDCa3pj&url={results}"
    res = requests.post(api)
    print(res.content)

file = open("moviesdb1.txt", "rt")
for line in file:
    getfilm(line)
#getfilm("https://mycima.me/مشاهدة-فيلم-rush-hour-2-2001-مترجم/")
