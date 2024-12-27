from fastapi import APIRouter, HTTPException, Depends
from models import Item, MongoDB

router = APIRouter()

@router.on_event("startup")
async def startup():
    MongoDB.connect()

@router.on_event("shutdown")
async def shutdown():
    MongoDB.close()

@router.get("/items", summary="Obtener todos los elementos")
async def get_items():
    items = await MongoDB.db["items"].find().to_list(100)
    return items

@router.get("/items/{item_id}", summary="Obtener un elemento por ID")
async def get_item(item_id: str):
    item = await MongoDB.db["items"].find_one({"_id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return item

@router.post("/items", summary="Crear un nuevo elemento")
async def create_item(item: Item):
    new_item = await MongoDB.db["items"].insert_one(item.dict(by_alias=True))
    created_item = await MongoDB.db["items"].find_one({"_id": new_item.inserted_id})
    return created_item

@router.delete("/items/{item_id}", summary="Eliminar un elemento")
async def delete_item(item_id: str):
    result = await MongoDB.db["items"].delete_one({"_id": item_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Elemento no encontrado")
    return {"message": "Elemento eliminado"}