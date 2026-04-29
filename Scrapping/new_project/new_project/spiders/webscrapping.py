# from urllib.parse import urlparse
# import scrapy

# class ExtractUrls(scrapy.Spider):
#     name = "extract"
#     allowed_domains = ['geeksforgeeks.org']
#     start_urls = ['https://www.geeksforgeeks.org/']
    
    

#     custom_settings = {
#         'FEED_FORMAT': 'json',
#         'FEED_URI': 'output.json',
#         'FEED_EXPORT_ENCODING': 'utf-8',
#     }


#     def parse(self, response):
#         t = response.css('title::text').get()  # Title
#         l = response.css('a::attr(href)').getall()  # Links
#         h1 = response.css('h1::text').getall()
#         pt=0

#         for url in l:
#             yield {
#                 't': t,  # Title
#                 'url': url,  # Link
#                 'h1 header':h1
#             }
            
#             #get top 2 links
#             links = response.css("a::attr(href)").getall()[:2]
            
            
#             for link in links:
#                 full_url= response.urljoin(link)
#                 yield scrapy.Request(url=full_url,callback=self.parse_link)
                
#     def parse_link(self,response):
#                     yield {
#                         "url":response.url,
#                         "content":response.css("body :: text").getall()
#                     }
                
                
                           

#             # Follow same-domain links
#             # if urlparse(url).netloc.endswith('geeksforgeeks.org'):
#             #     pt+=1
#             #     if pt==5:
#             #         print("scrappind done across 2 maximum links")
#             #         break
#             #     yield response.follow(url, callback=self.parse)
                
                
#                 # scrapy runspider my_spider.py
                
                
                
# from scrapy.crawler import CrawlerProcess

# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(ExtractUrls)
#     process.start()


import scrapy
from scrapy.crawler import CrawlerProcess


# class WikiSpider(scrapy.Spider):
#     name = "wiki_spider"

#     allowed_domains = ["en.wikipedia.org"]
#     start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]

#     custom_settings = {
#         "FEEDS": {
#             "output.json": {"format": "json", "encoding": "utf-8", "overwrite": True}
#         },
#         "DEPTH_LIMIT": 5,   # maximum crawl depth
#         "ROBOTSTXT_OBEY": True,
#         "LOG_LEVEL": "INFO",
#     }

#     visited_urls = set()

#     def extract_page_data(self, response, depth, parent_url):
#         """Extract page content"""
#         title = response.css("#firstHeading *::text").get()

#         paragraph = response.css(
#             "div.mw-parser-output > p:not(.mw-empty-elt)::text"
#         ).getall()

#         paragraph = "".join(paragraph[:5]).strip() if paragraph else ""

#         return {
#             "depth": depth,
#             "parent_url": parent_url,
#             "url": response.url,
#             "title": title.strip() if title else "No Title",
#             "first_text": paragraph[:200]
#         }

#     def parse(self, response):
#         """Recursive crawling function"""

#         depth = response.meta.get("depth", 1)
#         parent_url = response.meta.get("parent")

#         self.visited_urls.add(response.url)

#         # Extract data
#         yield self.extract_page_data(response, depth, parent_url)

#         # Stop if depth reached
#         if depth >= self.custom_settings["DEPTH_LIMIT"]:
#             return

#         links = response.css("div.mw-parser-output a::attr(href)").getall()

#         count = 0
#         for link in links:

#             if link.startswith("/wiki/") and ":" not in link:

#                 full_url = response.urljoin(link)

#                 if full_url not in self.visited_urls:

#                     self.visited_urls.add(full_url)

#                     yield scrapy.Request(
#                         full_url,
#                         callback=self.parse,
#                         meta={
#                             "depth": depth + 1,
#                             "parent": response.url
#                         }
#                     )

#                     count += 1

#                 if count == 3:  # limit links per page
#                     break


# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(WikiSpider)
#     process.start()

# # 3 links from main page. 
# # 2 link from each sub page

# import responses

# print("Depth :" , responses.meta.get("depth"))
#new 
import scrapy
from scrapy.crawler import CrawlerProcess


class WikiSpider(scrapy.Spider):
    name = "wiki"

    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Web_scraping"]

    custom_settings = {
        "FEEDS": {
            "output.json": {
                "format": "json",
                "encoding": "utf-8",
                "indent": 4,
                "overwrite": True,
            }
        },
        "ROBOTSTXT_OBEY": True,
        "LOG_LEVEL": "INFO",
        "ITEM_PIPELINES": {
            "pipelines.SqlitePipeline": 300,
        },
        "DEPTH_LIMIT": 2,
        "CONCURRENT_REQUESTS": 16,
        "DOWNLOAD_DELAY": 1,
    }

    def parse(self, response):
        print("URL:", response.url, "DEPTH:", response.meta.get("depth"))

        depth = response.meta.get("depth", 1)

        # Extract data including a small paragraph
        
        paragraphs = response.css("div.mw-parser-output > p::text").getall()
        # Take first 1–2 paragraphs, join them
        intro_text = " ".join(paragraphs[:2]).strip() if paragraphs else "No paragraph available"

        yield {
            "url": response.url,
            "title": response.css("#firstHeading::text").get() or "Unknown",
            "depth": depth,
            "snippet": intro_text,   
        }

        
        links = response.css("div.mw-parser-output a::attr(href)").getall()
        count = 0
        for link in links:
            if link.startswith("/wiki/") and ":" not in link:
                full_url = response.urljoin(link)

                yield scrapy.Request(
                    full_url,
                    callback=self.parse,
                )
                count += 1

                if count >= 3:
                    break
                
                
                
                
                
                
# for downloading the images 
import scrapy
from new_project.items import ImageItem
import scrapy
from new_project.items import ImageItem


class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = ["https://pixnio.com"]

    def parse(self, response):
        count = 0

        for src in response.css("img::attr(src)").getall():
            if count >= 2:
                break

            full_url = response.urljoin(src.strip())

            if full_url.startswith("http"):
                item = ImageItem()
                item["image_urls"] = [full_url]
                yield item
                count += 1
         
         
  # main code               
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(WikiSpider)
    process.start()