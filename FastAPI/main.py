from typing import Union
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# Configuració de templates i fitxers estàtics
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

class User(BaseModel):
    id: int
    nom: str = Field(..., min_length=2, max_length=50)
    cognom: str = Field(..., min_length=2, max_length=50)
    edat: int = Field(..., ge=0, le=120)
    email: EmailStr

# Simulem una base de dades d'usuaris
users_db = [
    User(id=1, nom="Joan", cognom="Garcia", edat=30, email="joan.garcia@example.com"),
    User(id=2, nom="Maria", cognom="López", edat=25, email="maria.lopez@example.com"),
    User(id=3, nom="Pere", cognom="Martí", edat=35, email="pere.marti@example.com"),
]

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("users_list.html", {"request": request, "users": users_db})

@app.get("/user/{user_id}")
async def user_detail(request: Request, user_id: int):
    user = next((user for user in users_db if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    return templates.TemplateResponse("user_detail.html", {"request": request, "user": user})

@app.post("/users")
async def create_user(user: User):
    users_db.append(user)
    return {"message": "Usuari creat correctament", "user_id": user.id}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    try:
        # Aquí aniria la lògica per actualitzar l'usuari a la base de dades
        for i, existing_user in enumerate(users_db):
            if existing_user.id == user_id:
                users_db[i] = user
                return {
                    "message": "Usuari actualitzat correctament",
                    "user_id": user_id,
                    "user_data": {
                        "nom": user.nom,
                        "cognom": user.cognom,
                        "edat": user.edat,
                        "email": user.email
                    }
                }
        raise HTTPException(status_code=404, detail="Usuari no trobat")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en actualitzar l'usuari: {str(e)}")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}