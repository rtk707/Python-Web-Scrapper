from cache import RedisCache
from mail import Mail
from mongodb import MongoDB
from scrapper import ProductScraper
import json
import os

scrapper = ProductScraper()
mongo_db = MongoDB()
cache = RedisCache()
mailer = Mail()

class Service:
    
    async def get_products(self, page_count) -> str:
        cached_data = cache.get('scrapped_data')
        if cached_data:
            return json.loads(cached_data)
        
        return self.scrape_data(page_count)
    
    async def scrape_data(self,page_count) -> str:
        final_data = []
        for page_index in range(page_count):
            url = f'{os.getenv("URL")}{page_index+1}'
            
            page_html = await scrapper.fetch(url)
            parsed_data = scrapper.parse(page_html)
            formatted_data = scrapper.format(parsed_data)
            final_data += formatted_data
        await mongo_db.insert_many('scrapped_data', final_data)
        file_name = os.getenv('OUTPUT_FILE_NAME')
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(final_data, json_file, indent=4, ensure_ascii=False)
            
        cache.set('scrapped_data', final_data)
        # mailer.send_email('Scrapping Status','Data Scrapped Successfully','ritikonweb2000@gmail.com')
        return "Data Scrapped Successfully"
