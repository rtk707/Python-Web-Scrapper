# controller.py
from fastapi import APIRouter
from service import Service

# Create an APIRouter object to define routes
router = APIRouter()
service = Service()

@router.get('/reload-cache/{page_count}')
async def get_products(page_count: int) -> str:
    return await service.reload_cache(page_count)

@router.get('/get-products/{page_count}')
async def get_products(page_count:int) -> str:
    return await service.get_products(page_count)