import scrapy


class JijiElectSpider(scrapy.Spider):
    name = "jiji_elect"
    allowed_domains = ["jiji.com.gh"]
    start_urls = ["https://jiji.com.gh/electronics"]

    def parse(self, response):
        pass
