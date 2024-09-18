import requests
from lxml import html

encabezados = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = "https://www.wikipedia.org/"

response = requests.get(url, headers = encabezados)

parser = html.fromstring(response.text)

### Obtenim eglissh desde lxml
# ingles = parser.get_element_by_id("js-link-box-en")
# print(ingles.text_content())

### Obtenim english desde xpath
# idiomas = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

# print(ingles)


### obtenim totes les llengues
idiomas = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")

for idioma in idiomas:
    print(idioma)
