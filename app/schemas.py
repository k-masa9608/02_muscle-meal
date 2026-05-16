from pydantic import BaseModel
from typing import List, Optional


class IngredientBase(BaseModel):
    name: str
    category: Optional[str] = None


class Ingredient(IngredientBase):
    id: int

    class Config:
        orm_mode = True


class RecipeIngredientOut(BaseModel):
    ingredient: Ingredient
    amount: Optional[str] = None

    class Config:
        orm_mode = True


class RecipeBase(BaseModel):
    name: str
    description: Optional[str] = None
    genre: Optional[str] = None
    protein: float = 0
    fat: float = 0
    carbs: float = 0
    calories: float = 0
    servings: int = 1
    cooking_time: Optional[int] = None


class RecipeOut(RecipeBase):
    id: int
    recipe_ingredients: List[RecipeIngredientOut] = []
    score: Optional[float] = None

    class Config:
        orm_mode = True


class SearchRequest(BaseModel):
    ingredients: List[str]
    limit: Optional[int] = 20
