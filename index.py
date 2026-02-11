from fastapi import FastAPI
app = FastAPI()
@app.get("/hello")
async def say_hello():
    return {"message": "Hello, World!"}