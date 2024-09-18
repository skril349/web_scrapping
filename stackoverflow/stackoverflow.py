import requests
from bs4 import BeautifulSoup
encabezados = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://es.stackoverflow.com/questions"

response = requests.get(url,headers=encabezados)

soup = BeautifulSoup(response.text)

contenedor_de_preguntas = soup.find(id="questions")
lista_de_preguntas = contenedor_de_preguntas.find_all('div',class_="s-post-summary--content")


for pregunta in lista_de_preguntas:
    texto_pregunta = pregunta.find('h3').text
    descripcion_pregunta = pregunta.find(class_='s-post-summary--content-excerpt').text
    descripcion_pregunta = descripcion_pregunta.replace('\n','').replace('\r','').strip()
    print("title = ",texto_pregunta)
    print("description = ",descripcion_pregunta)