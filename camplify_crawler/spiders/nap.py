import scrapy

from bs4 import BeautifulSoup

from camplify_crawler.items import CamplifyCrawlerItem


class NapSpider(scrapy.Spider):
    name = 'nap'
    allowed_domains = ['www.nap-camp.com']

    def start_requests(self):
        # TODO
        for page_id in range(2):
            yield scrapy.Request(
                f'https://www.nap-camp.com/kanagawa/list?sortId=21&pageId={page_id}'
            )
            print('foo')

    def parse(self, response):

        soup = BeautifulSoup(response.body, "html.parser")
        data = soup.find_all('li', class_='tab-content-item')

        if not data:
            print('page not found')
            return False

        for d in data:
            item = CamplifyCrawlerItem()
            item['name'] = d.find('h3', class_='name').text

            detail_page_path = d.find('a', class_='campsite-item')['href']
            detail_page_url = f'https://www.nap-camp.com{detail_page_path}'
            item['url'] = detail_page_url
            print(item)

            request = scrapy.Request(
                detail_page_url, callback=self.parse_detail)
            request.meta["item"] = item
            yield request

    def parse_detail(self, response):
        item = response.meta["item"]
        # TODO
        return item
