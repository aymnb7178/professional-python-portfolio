# Professional Python Portfolio

A growing collection of small Python projects. The collection is at an early stage: it currently contains **two** items, listed below.

## Current Projects

| Project | Description | Status |
|---|---|---|
| [`projects/meal-planner-nutrition-tracker`](projects/meal-planner-nutrition-tracker) | Streamlit app to pick meals from a small built-in list and track daily calories and macros | Prototype; its meal/nutrition logic is unit-tested, the Streamlit UI itself was not run by the assistant that refactored it |
| [`projects/fitness/fitness_calculator.py`](projects/fitness/fitness_calculator.py) | A single BMI function with a placeholder message | Example snippet. A tested BMI/BMR/TDEE version is in [fitness-calculator](https://github.com/aymnb7178/fitness-calculator) |

## Repository Structure

```
professional-python-portfolio/
├── README.md
├── .gitignore
└── projects/
    ├── fitness/
    │   └── fitness_calculator.py
    └── meal-planner-nutrition-tracker/
        ├── app.py
        ├── nutrition.py
        ├── test_nutrition.py
        ├── requirements.txt
        ├── README.md
        └── README.ar.md
```

## How to Run the Meal Planner

```bash
cd projects/meal-planner-nutrition-tracker
pip install -r requirements.txt
streamlit run app.py
```

## Tests

```bash
cd projects/meal-planner-nutrition-tracker
python -m unittest -v      # 4 tests for the meal data and totals (no Streamlit needed)
```

> The `nutrition.py` split and its tests were added with AI assistance (Claude), reviewed and published by the repository owner.

## Current Limitations

- Only one project is a runnable application; the BMI file is a short example.
- Meal data in the Meal Planner is a fixed list in the code, not a real nutrition database.

## Roadmap

The long-term goal is to grow this collection into a larger set of Python projects (the earlier description mentioned a target of 60). New projects will be added here only once their code exists.

## Author

Aymen — [github.com/aymnb7178](https://github.com/aymnb7178)
