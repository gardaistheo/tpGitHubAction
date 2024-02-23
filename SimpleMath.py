import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b
    @staticmethod
    def soustraction(a, b):
        return a - b

class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(3, 5)
        self.assertEqual(result, 8, "La fonction addition ne retourne pas le résultat attendu")
    def test_soustraction(self):
        result = SimpleMath.soustraction(5, 3)
        self.assertEqual(result, 2, "La fonction soustraction ne retourne pas le résultat attendu")

if __name__ == "__main__":
    unittest.main()
