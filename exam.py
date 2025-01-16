def get_days_in_month(month):
    days_in_month = {
        "січень": 31,
        "лютий": 28,  # Для простоти будемо рахувати тільки непереступні роки
        "березень": 31,
        "квітень": 30,
        "травень": 31,
        "червень": 30,
        "липень": 31,
        "серпень": 31,
        "вересень": 30,
        "жовтень": 31,
        "листопад": 30,
        "грудень": 31
    }
    if month.lower() in days_in_month:
        return days_in_month[month.lower()]
    else:
        raise ValueError("Невідомий місяць")

# Приклад виклику функції
print(get_days_in_month("травень"))  # Виведе 31
try:
    print(get_days_in_month("полуниця"))  # Генерує ValueError
except ValueError as e:
    print(e)
import unittest

class TestGetDaysInMonth(unittest.TestCase):
    def test_valid_months(self):
        self.assertEqual(get_days_in_month("січень"), 31)
        self.assertEqual(get_days_in_month("лютий"), 28)
        self.assertEqual(get_days_in_month("квітень"), 30)

    def test_invalid_month(self):
        with self.assertRaises(ValueError):
            get_days_in_month("абрикосень")

if __name__ == "__main__":
    unittest.main()
