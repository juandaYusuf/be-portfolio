from fastapi import FastAPI
from routers.request_method import api



app = FastAPI()

routers = [api]

for router in routers:
    app.include_router(router)
