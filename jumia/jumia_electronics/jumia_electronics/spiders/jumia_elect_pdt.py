import scrapy


class JumiaElectPdtSpider(scrapy.Spider):
    name = "jumia_elect_pdt"
    allowed_domains = ["jumia.com.gh"]
    start_urls = ["https://jumia.com.gh/electronics/"]


    def parse(self, response):
        # Navigate through each product using the article selector
        for product in response.css("article.prd._fb.col.c-prd"):
            
            # Extracting product link
            product_link = product.css("a.core::attr(href)").extract_first()
            
            # Extracting image URL
            image_url = product.css("div.img-c > img.img::attr(data-src)").extract_first()
            
            # Extracting product name
            product_name = product.css("h3.name::text").extract_first().strip()
            
            # Extracting product price
            product_price = product.css("div.prc::text").extract_first().strip()

            yield {
                'product_link': product_link,
                'image_url': image_url,
                'product_name': product_name,
                'product_price': product_price
            }

# Command to run the spider and save the output to a JSON file:
# scrapy crawl jum-elect-spider -o output.json
