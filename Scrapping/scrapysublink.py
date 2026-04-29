from urllib.parse import urlparse
import scrapy

class ExtractUrls(scrapy.Spider):
    name = "extract"
    allowed_domains = ['geeksforgeeks.org']
    start_urls = ['https://www.geeksforgeeks.org/']
    


    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
        'FEED_EXPORT_ENCODING': 'utf-8',
    }


    def parse(self, response):
        t = response.css('title::text').get()  # Title
        l = response.css('a::attr(href)').getall()  # Links

        for url in l:
            yield {
                't': t,  # Title
                'url': url  # Link
            }

            # Follow same-domain links
            if urlparse(url).netloc.endswith('geeksforgeeks.org'):
                yield response.follow(url, callback=self.parse)