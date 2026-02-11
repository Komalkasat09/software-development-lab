from fastapi import FastAPI
from bson import ObjectId

from .schemas import CartItem
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27019/")
db = client.ecommerce
cart_collection = db.carts

@app.post("/cart/{user_id}")
async def create_cart(user_id: str):
    cart = {
        "user_id": user_id,
        "items": [],
        "total_price": 0
    }
    result = await db.carts.insert_one(cart)
    return {"cart_id": str(result.inserted_id)}

@app.post("/cart/{cart_id}/add")
async def add_item(cart_id: str, item: CartItem):
    await db.carts.update_one(
        {"_id": ObjectId(cart_id)},
        {"$push": {"items": item.dict()}}
    )
    return {"message": "Item added"}

@app.get("/cart/{cart_id}")
async def get_cart(cart_id: str):
    cart = await db.carts.find_one({"_id": ObjectId(cart_id)})
    cart["_id"] = str(cart["_id"])
    return cart