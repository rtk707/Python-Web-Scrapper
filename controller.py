# controller.py
from fastapi import APIRouter
from input_dto import InputRequest
from service import Service

# Create an APIRouter object to define routes
router = APIRouter()
service = Service()

@router.post('/reload-cache')
async def get_products(req: InputRequest) -> str:
    return await service.reload_cache(req.page_count, req.proxy_string)

@router.get('/get-products')
async def get_products(req:InputRequest) -> str:
    return await service.get_products(req.page_count, req.proxy_string)