from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from bson import ObjectId

# Pydantic Model para validar datos
class Item(BaseModel):
    id: str = Field(default=None, alias="_id")
    name: str
    price: float

# Función para inicializar la conexión
class MongoDB:
    client: AsyncIOMotorClient = None

    @staticmethod
    def connect():
        MongoDB.client = AsyncIOMotorClient("mongodb://mongo:27017")
        MongoDB.db = MongoDB.client["items_db"]

    @staticmethod
    def close():
        MongoDB.client.close()