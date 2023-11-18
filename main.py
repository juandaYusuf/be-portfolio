from fastapi import FastAPI
from routers.request_method import api



app = FastAPI()

routers = [api]

for router in routers:
    app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)