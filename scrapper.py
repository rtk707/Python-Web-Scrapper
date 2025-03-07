from requests_html import HTMLSession
from typing import Dict, List

from tenacity import retry, stop_after_attempt, wait_fixed

class ProductScraper:
    def __init__(self):
        self.proxy = {
            "http": "http://36.64.6.5:8080",
            "https": "http://36.64.6.5:8080"
        }
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
    async def fetch(self, url: str) -> str:
        try:
            session = HTMLSession()
            response = session.get(url)
            return response
        except:
            raise    
    def parse(self, html_data: str) -> List[Dict]:
        # Use the HTML response to extract product information
        product_tags = html_data.html.find('div.product-inner')
        products = []

        for product_tag in product_tags:
            product_id = product_tag.find('div.addtocart-buynow-btn a')[0].attrs['data-product_id']
            title = product_tag.find('div.addtocart-buynow-btn a')[0].attrs['data-title']
            price = product_tag.find('span.woocommerce-Price-amount', first=1).text
            image = product_tag.find('img.size-woocommerce_thumbnail')[0].attrs['data-lazy-src']
            
            product_data = {
                'product_id': product_id,
                'title': title,
                'price': price,
                'image': image
            }
            
            products.append(product_data)
        return products