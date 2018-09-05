import requests
from bs4 import BeautifulSoup

response_obj = requests.get("https://www.youtube.com/feed/trending")

if response_obj.status_code == 200:
    soup = BeautifulSoup(response_obj.text, 'html.parser')
    elements = soup.find_all("div", "yt-lockup-content")
    for i in elements:
        title = i.contents[0].contents[0].text
        hrefd = i.contents[0].contents[0]["href"]
        time = i.contents[2].contents[0].contents[0].text
        print("Название: " + title + "   Ссылка: " + hrefd + "    Дата: " + time)
        