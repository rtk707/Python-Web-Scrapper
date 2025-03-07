# controller.py
from fastapi import APIRouter
# from cache import RedisCache
from service import Service

# Create an APIRouter object to define routes
router = APIRouter()
service = Service()
# cache = RedisCache()

@router.get("/update-cache/{page_count}")
async def get_products(page_count: int) -> str:
    return await service.scrape_data(page_count)

@router.get('get-products')
    return await serive.update_cache()