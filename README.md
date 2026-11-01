# Professional Python Portfolio

A growing collection of small Python projects. The collection is at an early stage: it currently contains **two** items, listed below.

## Current Projects

| Project | Description | Status |
|---|---|---|
| [`projects/meal-planner-nutrition-tracker`](projects/meal-planner-nutrition-tracker) | Streamlit app to pick meals from a small built-in list and track daily calories and macros | Working prototype |
| [`projects/fitness/fitness_calculator.py`](projects/fitness/fitness_calculator.py) | A single BMI function with a placeholder message | Example snippet |

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

## Current Limitations

- Only one project is a runnable application; the BMI file is a short example.
- Meal data in the Meal Planner is a fixed list in the code, not a real nutrition database.

## Roadmap

The long-term goal is to grow this collection into a larger set of Python projects (the earlier description mentioned a target of 60). New projects will be added here only once their code exists.

## Author

Aymen — [github.com/aymnb7178](https://github.com/aymnb7178)
