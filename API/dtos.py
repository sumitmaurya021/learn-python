from pydantic import BaseModel

class ProductDTO(BaseModel):
    id: int
    name: str
    price: float
    category: str
    stock: int
