from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "category": "Electronics",
        "description": "High performance laptop",
        "image": "https://via.placeholder.com/200",
        "stock": 10
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 25000,
        "category": "Electronics",
        "description": "Android smartphone",
        "image": "https://via.placeholder.com/200",
        "stock": 15
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000,
        "category": "Accessories",
        "description": "Wireless headphones",
        "image": "https://via.placeholder.com/200",
        "stock": 20
    },
    {
        "id": 4,
        "name": "Keyboard",
        "price": 1500,
        "category": "Accessories",
        "description": "Mechanical keyboard",
        "image": "https://via.placeholder.com/200",
        "stock": 30
    },
    {
        "id": 5,
        "name": "Mouse",
        "price": 800,
        "category": "Accessories",
        "description": "Gaming mouse",
        "image": "https://via.placeholder.com/200",
        "stock": 25
    },
    {
        "id": 6,
        "name": "Monitor",
        "price": 12000,
        "category": "Electronics",
        "description": "24-inch monitor",
        "image": "https://via.placeholder.com/200",
        "stock": 12
    },
    {
        "id": 7,
        "name": "Smart Watch",
        "price": 5000,
        "category": "Wearables",
        "description": "Fitness smartwatch",
        "image": "https://via.placeholder.com/200",
        "stock": 18
    },
    {
        "id": 8,
        "name": "Speaker",
        "price": 2500,
        "category": "Audio",
        "description": "Bluetooth speaker",
        "image": "https://via.placeholder.com/200",
        "stock": 14
    },
    {
        "id": 9,
        "name": "Printer",
        "price": 7000,
        "category": "Office",
        "description": "Color printer",
        "image": "https://via.placeholder.com/200",
        "stock": 8
    },
    {
        "id": 10,
        "name": "Webcam",
        "price": 1800,
        "category": "Accessories",
        "description": "HD webcam",
        "image": "https://via.placeholder.com/200",
        "stock": 22
    }
]

@app.get("/")
def home():
    return {"message": "FastAPI E-Commerce API"}

@app.get("/products")
def get_products():
    return products