from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from . import models


def get_all_ingredients(db: Session):
    return db.query(models.Ingredient).order_by(models.Ingredient.category, models.Ingredient.name).all()


def search_recipes(db: Session, ingredient_names: List[str], limit: int = 20):
    if not ingredient_names:
        results = db.query(models.Recipe).all()
    else:
        normalized = [n.strip() for n in ingredient_names if n.strip()]
        matched_ids_q = (
            db.query(models.RecipeIngredient.recipe_id)
            .join(models.Ingredient)
            .filter(models.Ingredient.name.in_(normalized))
            .group_by(models.RecipeIngredient.recipe_id)
            .having(func.count(models.RecipeIngredient.recipe_id) >= 1)
        )
        results = db.query(models.Recipe).filter(models.Recipe.id.in_(matched_ids_q)).all()

    def score(r):
        fat_penalty = r.fat if r.fat > 0 else 0
        return r.protein * 2 - fat_penalty

    results.sort(key=score, reverse=True)

    for r in results:
        r.score = round(score(r), 1)

    return results[:limit]


def get_recipe(db: Session, recipe_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
