import scrapy

from bs4 import BeautifulSoup


class NapSpider(scrapy.Spider):
    name = 'nap'
    allowed_domains = ['www.nap-camp.com']
    start_urls = [
        'https://www.nap-camp.com/kanagawa/list?sortId=21&pageId=1'
    ]

    def parse(self, response):
        soup = BeautifulSoup(response.body, "html.parser")
        items = soup.find_all('li', class_='tab-content-item')

        for item in items:
            name = item.find('h3', class_='name').text
            print(name)
