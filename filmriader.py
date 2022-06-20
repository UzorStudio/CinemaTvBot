import requests
from bs4 import BeautifulSoup

def getFilm():
    url = "https://tvfeed.in/film/random/"
    film = {}


    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.text, 'lxml')
    film["ru_name"] = soup.find('h1', class_="f32").text
    film["en_name"] = soup.find('h3').text
    quiclink = soup.find_all('p')
    film["cuntry"] = quiclink[0].text.replace("\n","")
    film["ear"] = quiclink[1].text.replace("\n","")
    genre1 = (quiclink[2].text.replace("\n","").replace(" ","").split(","))
    genre = []

    for g in genre1:
         genre.append("#"+g)


    film["genre"] = " ".join(genre)

    urlGoogle = f"https://www.google.com/search?q=youtube+{film['ru_name']} {film['ear']} русский трейлер"

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    google = requests.get(urlGoogle, headers=headers)
    soup2 = BeautifulSoup(google.text, 'lxml')
    film["youtubeLink"] = soup2.find('div', class_="ct3b9e").find("a").get("href")

    print(film)

    return film

getFilm()