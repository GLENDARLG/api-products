from fastapi import FastAPI
from routers import router

app = FastAPI(
    title="API RESTful con MongoDB",
    description="Una API RESTful conectada a MongoDB",
    version="1.0.0",
)

app.include_router(router)