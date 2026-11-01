# Meal Planner & Nutrition Tracker

A small Streamlit app for choosing meals and tracking daily calories and macronutrients. It is a prototype that works with a fixed list of eight sample meals.

> النسخة العربية: [README.ar.md](README.ar.md)

## Overview

Pick a meal type, choose a suggested meal, and add it to a daily log. The app sums calories, protein, carbs, and fat and compares them with the goals set in the sidebar.

## Key Features

- Daily calorie goal and protein / carbs / fat goals (sidebar inputs)
- Meal suggestions filtered by type: Breakfast, Lunch, Dinner, Snack
- Daily log table with totals compared against the goals
- Button to clear the daily log

## Technologies Used

- Python 3
- Streamlit 1.38.0
- pandas 2.2.2

## Project Structure

```
meal-planner-nutrition-tracker/
├── app.py
├── requirements.txt
├── README.md
└── README.ar.md
```

## Installation

```bash
pip install -r requirements.txt
```

## How to Run

```bash
streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Current Limitations

- Meals come from a hard-coded list of eight items, not a real nutrition database.
- The log is kept in Streamlit `session_state`, so it resets when the session ends.
- Suggestions are filtered by meal type only; they do not adapt to the calorie or macro goals.
- No tests.

## Future Improvements

- Use a recipe / nutrition API instead of the fixed list
- Personalized suggestions based on goals and preferences
- Weekly reports

## Author

Aymen — [github.com/aymnb7178](https://github.com/aymnb7178)
