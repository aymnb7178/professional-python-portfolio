"""Meal data and nutrition maths for the Meal Planner (no Streamlit needed, so it is testable)."""
from typing import Dict, Iterable, List

MEAL_TYPES = ["Breakfast", "Lunch", "Dinner", "Snack"]

# Small hand-written sample list (values are approximate examples, not a nutrition database)
MEALS = [
    {"name": "بيض مسلوق + خبز كامل", "calories": 350, "protein": 25, "carbs": 30, "fat": 15, "type": "Breakfast"},
    {"name": "شوفان مع فواكه", "calories": 280, "protein": 8, "carbs": 45, "fat": 6, "type": "Breakfast"},
    {"name": "سلطة دجاج مشوي", "calories": 450, "protein": 40, "carbs": 10, "fat": 25, "type": "Lunch"},
    {"name": "رز بني + سمك مشوي", "calories": 520, "protein": 35, "carbs": 55, "fat": 12, "type": "Lunch"},
    {"name": "سلطة خضراوات + توفو", "calories": 320, "protein": 18, "carbs": 20, "fat": 18, "type": "Dinner"},
    {"name": "دجاج مشوي + بطاطس مشوية", "calories": 480, "protein": 38, "carbs": 35, "fat": 20, "type": "Dinner"},
    {"name": "يوغورت يوناني + مكسرات", "calories": 200, "protein": 15, "carbs": 25, "fat": 5, "type": "Snack"},
    {"name": "تفاحة + لوز", "calories": 180, "protein": 5, "carbs": 25, "fat": 8, "type": "Snack"},
]


def meals_of_type(meal_type: str) -> List[dict]:
    return [m for m in MEALS if m["type"] == meal_type]


def totals(logged: Iterable[dict]) -> Dict[str, int]:
    """Sum calories / protein / carbs / fat over logged meals."""
    out = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for meal in logged:
        for k in out:
            out[k] += meal[k]
    return out
