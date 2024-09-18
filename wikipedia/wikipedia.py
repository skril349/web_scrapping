import requests
from lxml import html

encabezados = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
url = "https://www.wikipedia.org/"

response = requests.get(url, headers = encabezados)

parser = html.fromstring(response.text)

# ingles = parser.get_element_by_id("js-link-box-en")
# print(ingles.text_content())

ingles = parser.xpath("//a[@id='js-link-box-en']/strong/text()")

print(ingles)