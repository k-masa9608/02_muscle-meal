from .database import SessionLocal, engine
from . import models
from .seed_data import INGREDIENTS, RECIPES


def seed():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(models.Recipe).count() > 0:
        db.close()
        return

    ingredient_map = {}
    for name, category in INGREDIENTS:
        ing = models.Ingredient(name=name, category=category)
        db.add(ing)
        db.flush()
        ingredient_map[name] = ing.id

    for r in RECIPES:
        recipe = models.Recipe(
            name=r["name"],
            description=r.get("description"),
            genre=r.get("genre"),
            protein=r.get("protein", 0),
            fat=r.get("fat", 0),
            carbs=r.get("carbs", 0),
            calories=r.get("calories", 0),
            servings=r.get("servings", 2),
            cooking_time=r.get("cooking_time"),
        )
        db.add(recipe)
        db.flush()

        for ing_name, amount in r.get("ingredients", []):
            ing_id = ingredient_map.get(ing_name)
            if ing_id:
                ri = models.RecipeIngredient(
                    recipe_id=recipe.id,
                    ingredient_id=ing_id,
                    amount=amount,
                )
                db.add(ri)

    db.commit()
    db.close()
    print(f"Seeded {len(RECIPES)} recipes.")
