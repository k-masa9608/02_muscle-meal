import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List

from .database import engine, get_db
from . import models, crud, schemas
from .seed import seed

models.Base.metadata.create_all(bind=engine)
seed()

app = FastAPI(title="Muscle Meal", version="1.0.0")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def read_root():
    return FileResponse(os.path.join(STATIC_DIR, "index.html"))


@app.get("/api/ingredients", response_model=List[schemas.Ingredient])
def get_ingredients(db: Session = Depends(get_db)):
    return crud.get_all_ingredients(db)


@app.post("/api/search", response_model=List[schemas.RecipeOut])
def search_recipes(req: schemas.SearchRequest, db: Session = Depends(get_db)):
    return crud.search_recipes(db, req.ingredients, req.limit or 20)


@app.get("/api/recipes/{recipe_id}", response_model=schemas.RecipeOut)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = crud.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe
