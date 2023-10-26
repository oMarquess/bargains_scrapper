import scrapy

class MelcomElectPdtSpider(scrapy.Spider):
    name = "melcom_elect_pdt"
    allowed_domains = ["melcom.com"]
    start_urls = ["https://melcom.com/categories/electronics-appliances.html"]

    def parse(self, response):
        for product in response.css('li.product.product-item'):
            # Extracting product image
            image_url = product.css('.product-image-photo::attr(src)').get()

            # Extracting product name
            product_name = product.css('.product.name.product-item-name a::text').get()

            # Extracting product special price and regular price
            special_price = product.css('.special-price .price::text').get()
            regular_price = product.css('.old-price .price::text').get()

            yield {
                'image_url': image_url,
                'product_name': product_name,
                'special_price': special_price,
                'regular_price': regular_price,
            }
