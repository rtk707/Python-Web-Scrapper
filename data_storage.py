import json
import os


class DataStorage:
    
    async def save_as_json(self, data: list):
        file_name = os.getenv('OUTPUT_FILE_NAME')
        with open(file_name, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)