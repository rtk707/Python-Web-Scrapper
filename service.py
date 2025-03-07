from cache import RedisCache
from data_storage import DataStorage
from mail import Mail
from mongodb import MongoDB
from scrapper import ProductScraper
import json
import os

scrapper = ProductScraper()
mongo_db = MongoDB()
cache = RedisCache()
mailer = Mail()
data_storage = DataStorage()

class Service:
    
    async def reload_cache(self, page_count, proxy_string) -> str:
        return await self.scrape_data(page_count, proxy_string)
    
    async def get_products(self, page_count, proxy_string) -> str:
        cached_data = cache.get('scrapped_data')
        if cached_data:
            return json.loads(cached_data)
        return await self.scrape_data(page_count, proxy_string)
    
    async def scrape_data(self, page_count, proxy_string) -> str:
        final_data = []
        
        for page_index in range(page_count):    
            url = f'{os.getenv("URL")}{page_index+1}'
            page_html = await scrapper.fetch(url, proxy_string)
            parsed_data = scrapper.parse(page_html)
            final_data += parsed_data
            
            
        await mongo_db.insert_many('scrapped_data', final_data)
        file_name = os.getenv('OUTPUT_FILE_NAME')
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(final_data, json_file, indent=4, ensure_ascii=False)
            
        update_count = cache.update_cache(final_data, 'scrapped_data')
            
        mailer.send_email('Scrapping Status', f'Successfully Updated {update_count} records','ritikonweb2000@gmail.com')
        return "Data Scrapped Successfully"
