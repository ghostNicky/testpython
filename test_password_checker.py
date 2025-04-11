import unittest
from password_checker import is_valid_password

class TestPasswordChecker(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(is_valid_password("StrongPass1"))
    
    def test_short_password(self):
        self.assertFalse(is_valid_password("Srt1"))
    
    def test_no_digit(self):
        self.assertFalse(is_valid_password("StrongPass"))
    
    def test_no_uppercase(self):
        self.assertFalse(is_valid_password("strongpass1"))

if __name__ == "__main__":
    unittest.main()
