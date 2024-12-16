from fastapi import FastAPI
from routes.cat import router as cat_router

app = FastAPI()

app.include_router(cat_router)

@app.get("/")
def my_cool_function():
    return {"message": "Hello World"}
