import requests
from bs4 import BeautifulSoup

def getfilm(url):
    links = []
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a'):
        lin = link.get('href')
        if"live" in lin:
            links.append(lin)
    #print(links)
    for link in links:
        if "1080" in link:
            print("download in 1080p : " + link)
        if "720" in link:
            print("download in 720p : " + link)
        if "480" in link:
            print("download in 480p : " + link)
        if "360" in link:
            print("download in 360p : " + link)
            
films = ["https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Zack-and-Miri-Make-a-Porno-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Youth-in-Revolt-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-You-Will-Meet-a-Tall-Dark-Stranger-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-When-in-Rome-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-What-Happens-in-Vegas-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Water-For-Elephants-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-WALL-E-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Waitress-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Waiting-For-Forever-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Valentine's-Day-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Tyler-Perry's-Why-Did-I-get-Married-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Twilight:-Breaking-Dawn-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Twilight-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Ugly-Truth-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Twilight-Saga:-New-Moon-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Time-Traveler's-Wife-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Proposal-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Invention-of-Lying-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Heartbreak-Kid-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Duchess-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Curious-Case-of-Benjamin-Button-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-The-Back-up-Plan-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Tangled-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Something-Borrowed-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-She's-Out-of-My-League-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Sex-and-the-City-Two-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Sex-and-the-City-2-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Sex-and-the-City-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Remember-Me-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Rachel-Getting-Married-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Penelope-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-P.S.-I-Love-You-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Over-Her-Dead-Body-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Our-Family-Wedding-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-One-Day-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Not-Easily-Broken-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-No-Reservations-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Nick-and-Norah's-Infinite-Playlist-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-New-Year's-Eve-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-My-Week-with-Marilyn-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Music-and-Lyrics-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Monte-Carlo-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Miss-Pettigrew-Lives-for-a-Day-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Midnight-in-Paris-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Marley-and-Me-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Mamma-Mia!-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Mamma-Mia!-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Made-of-Honor-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Love-Happens-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Love-&-Other-Drugs-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Life-as-We-Know-It-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-License-to-Wed-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Letters-to-Juliet-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Leap-Year-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Knocked-Up-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Killers-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Just-Wright-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Jane-Eyre-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-It's-Complicated-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-I-Love-You-Phillip-Morris-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-High-School-Musical-3:-Senior-Year-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-He's-Just-Not-That-Into-You-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Good-Luck-Chuck-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Going-the-Distance-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Gnomeo-and-Juliet-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Gnomeo-and-Juliet-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Ghosts-of-Girlfriends-Past-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Four-Christmases-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Fireproof-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Enchanted-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Dear-John-2010-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Beginners-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-Across-the-Universe-2007-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-A-Serious-Man-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-A-Dangerous-Method-2011-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-27-Dresses-2008-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",
"https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-500-Days-of-Summer-2009-%d9%85%d8%aa%d8%b1%d8%ac%d9%85/",]

#getfilm("https://mycima.me/%d9%85%d8%b4%d8%a7%d9%87%d8%af%d8%a9-%d9%81%d9%8a%d9%84%d9%85-meka-suri-2020-%d9%85%d8%aa%d8%b1%d8%ac%d9%85-2/")









for f in films:
    getfilm(f)











