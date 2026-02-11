from pydantic import BaseModel
from typing import List

class CartItem(BaseModel):
    product_id: str
    name: str
    price: int
    quantity: int

class Cart(BaseModel):
    user_id: str
    items: List[CartItem]
    total_price: int