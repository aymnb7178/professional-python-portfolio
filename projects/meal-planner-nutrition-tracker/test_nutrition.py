import unittest

from nutrition import MEAL_TYPES, MEALS, meals_of_type, totals


class TestNutrition(unittest.TestCase):
    def test_every_type_has_meals_and_valid_fields(self):
        for t in MEAL_TYPES:
            self.assertTrue(meals_of_type(t), t)
        for m in MEALS:
            self.assertIn(m["type"], MEAL_TYPES)
            for k in ("calories", "protein", "carbs", "fat"):
                self.assertGreater(m[k], 0)

    def test_totals(self):
        logged = [MEALS[0], MEALS[2]]
        self.assertEqual(totals(logged), {"calories": 800, "protein": 65, "carbs": 40, "fat": 40})

    def test_totals_empty(self):
        self.assertEqual(totals([]), {"calories": 0, "protein": 0, "carbs": 0, "fat": 0})

    def test_unknown_type_is_empty(self):
        self.assertEqual(meals_of_type("Brunch"), [])


if __name__ == "__main__":
    unittest.main()
