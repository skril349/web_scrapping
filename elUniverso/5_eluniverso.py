"""
OBJETIVO: 
    - Extraer los titulares y el resumen de las noticias en la pagina principal de deportes de EL UNIVERSO.
    - Contrastar el uso de Beautiful Soup y Scrapy para parsear el arbol HTML.
CREADO POR: LEONARDO KUFFO
ULTIMA VEZ EDITADO: 16 ENERO 2024
"""

from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess

# ABSTRACCION DE DATOS A EXTRAER - DETERMINA LOS DATOS QUE TENGO QUE LLENAR Y QUE ESTARAN EN EL ARCHIVO GENERADO
class Noticia(Item):
    id = Field()
    titular = Field()
    descripcion = Field()


# CLASE CORE - SPIDER  
class ElUniversoSpider(Spider):
    name = "MiSegundoSpider"
    custom_settings = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        # 'FEED_EXPORT_FIELDS': ['id', 'descripcion', 'titular'], # Como ordenar las columnas en el CSV?
        # 'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes 
        #'FEED_EXPORT_ENCODING': 'utf-8'
    }
    start_urls = ['https://www.eluniverso.com/deportes']

    def parse(self, response):
        sel = Selector(response)
        noticias = sel.xpath('/html/body/div/section/div/div/div/div/div/ul/li')
        
        for i, elem in enumerate(noticias): # PARA INVESTIGAR: Para que sirve enumerate?
            item = ItemLoader(Noticia(), elem) # Cargo mi item

            # Llenando mi item a traves de expresiones XPATH
            item.add_xpath('titular', './/h2/a/text()')
            item.add_xpath('descripcion', './/p/text()')
            item.add_value('id', i)
            yield item.load_item() # Retorno mi item lleno



# EJECUCION POR TERMINAL
# python -m scrapy runspider .\5_eluniverso.py -o resultados.csv

# CORRIENDO SCRAPY SIN LA TERMINAL
# python ./5_eluniverso.py
process = CrawlerProcess({
    'FEED_FORMAT': 'json',
    'FEED_URI': 'datos_de_salida.json'
})
process.crawl(ElUniversoSpider)
process.start()