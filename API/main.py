from fastapi import FastAPI, Request
from mockData import products
from dtos import ProductDTO

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to FastAPI Series!"


@app.get("/products")
def get_products():
    return products


# Path params..
@app.get("/products/{product_id}")
def get_one_product(product_id:int):
    
    for product in products:
        if product.get("id") == product_id:
            return product
    
    return "No Product Found"


# Query params..
@app.get("/greet")
def greet_user(request:Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "Message": f"Hello {query_params.get('name')} your age is {query_params.get('age')}"
    }

# diffrent types of HTTP Methods

@app.post("/create_product")
def create_product(product_data:ProductDTO):
    product_data = product_data.model_dump()
    products.append(product_data)
    return {"data": products, "status": "Product Created Successfully..."}


@app.put("/update_product/{product_id}")
def update_product(product_data:ProductDTO, product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = product_data.model_dump()
            return {"status": "Product update ssuccesfully", "product": product_data}
            
    return {"status": f"Product Not Found {product_id}"}


@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index, oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            deleted_product = products.pop(index)
            return {"status": "Product deleted ssuccesfully", "product": deleted_product}
    
    return {"status": f"Product Not Found {product_id}"}


# How to call diffrent HTTP Methods. Any tool?
# how to validate data. - DTOS.

