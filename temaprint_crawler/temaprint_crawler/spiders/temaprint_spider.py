import scrapy

class TemaPrintSpider(scrapy.Spider):
    name = 'icons8'
    allowed_domains = ['blog.icons8.com']
    start_urls = ['https://blog.icons8.com']

    custom_settings = {
        'DEPTH_LIMIT': 5,
        'ROBOTSTXT_OBEY': True,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    def parse(self, response):
        # Extract and print the URL
        yield {'url': response.url}

        # Follow all internal links
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)
