import requests
from bs4 import BeautifulSoup
encabezados = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://news.ycombinator.com/"

response = requests.get(url,headers=encabezados)

soup = BeautifulSoup(response.text, "lxml")

lista_de_noticias = soup.find_all("tr",class_="athing")
for noticia in lista_de_noticias:
    title = noticia.find("span", class_="titleline").text
    url_ = noticia.find("span", class_="titleline").find("a").get("href")
    metadata = noticia.find_next_sibling()
    # score_tag = metadata.find("span", class_="score") if metadata else None
    # score = score_tag.text if score_tag else "No score"
    try:
        score = metadata.find("span", class_="score").text
    except:
        score = "No Score"
    
    subtext = metadata.find("td", class_="subtext") if metadata else None
    comentarios = subtext.find_all("a")[-1].text if subtext and len(subtext.find_all("a")) > 1 else "No comments"
    
    print(title)
    print(url_)
    print("score = ", score)
    print("Comments = ", comentarios)
