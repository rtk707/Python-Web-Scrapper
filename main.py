import os
from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from auth import Auth
from controller import router

app = FastAPI()
load_dotenv()
static_token = os.getenv("STATIC_TOKEN")
auth = Auth(static_token)

app.include_router(router, dependencies=[Depends(auth.verify_token)])
