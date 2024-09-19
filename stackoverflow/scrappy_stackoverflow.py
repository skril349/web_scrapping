import sys
import asyncio
from twisted.internet import asyncioreactor

# Comprova si el bucle d'events és ProactorEventLoop i substitueix-lo per SelectorEventLoop
if isinstance(asyncio.get_event_loop(), asyncio.ProactorEventLoop):
    asyncio.set_event_loop(asyncio.SelectorEventLoop())

# Instal·la el reactor compatible amb asyncio
asyncioreactor.install(asyncio.get_event_loop())


from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


class Pregunta(Item):
    # camps que volem extreure
    pregunta = Field()
    descripcion = Field()


class StackOverflowSpider(Spider):
    name = "MiPrimerSpider"
    custom_settings = {
        "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    start_urls = ["https://es.stackoverflow.com/questions"]

    def parse(self, response):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="questions"]//div[contains(@class, "s-post-summary")]')
        print(f"Trobades {len(preguntas)} preguntes.")
        for pregunta in preguntas:
            item = ItemLoader(item=Pregunta(), selector=pregunta)  
            item.add_xpath('pregunta', './/h3/a/text()')
            item.add_xpath('descripcion', './/div[@class="s-post-summary--content-excerpt"]/text()')

            # Només fa yield si pregunta i descripcion tenen valors
            loaded_item = item.load_item()
            if loaded_item.get('pregunta') and loaded_item.get('descripcion'):
                yield loaded_item
