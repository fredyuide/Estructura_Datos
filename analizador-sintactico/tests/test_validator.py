import unittest
from src.validator import validate_expression

class TestValidator(unittest.TestCase):
    def test_valid_expressions(self):
        self.assertTrue(validate_expression("((a + b) * c)")["valid"])
        self.assertTrue(validate_expression("5 * (3 + 2)")["valid"])

    def test_invalid_expressions(self):
        self.assertFalse(validate_expression("((a + b) * c")["valid"])
        self.assertFalse(validate_expression("(5 * [3 + 2)}")["valid"])
        self.assertFalse(validate_expression("(5 * 3 + 2) &")["valid"])

if __name__ == "__main__":
    unittest.main()
