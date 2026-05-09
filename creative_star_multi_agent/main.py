
from fastapi import FastAPI
from api.workflow import router

app = FastAPI(title="Creative Star")

app.include_router(router)
