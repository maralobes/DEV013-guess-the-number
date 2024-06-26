import unittest
from main import generate_secret_number, validate_user_input, check_guess

class TestGuessingTheNumber(unittest.TestCase):
    def setUp(self):
        ''''These are recurrent variables needed in the whole test.'''
        self.lower_number = 1
        self.upper_number = 100
        self.user_valid_guess = 60
    def test_generate_secret_number(self):
        ''''This test validate if the secrect number is into the correct limits.'''
        secret_number = generate_secret_number(self.lower_number, self.upper_number)
        self.assertTrue(self.lower_number <= secret_number <= self.upper_number)
    def test_validate_user_input(self):
        user_invalid_range_input = 150
        self.assertTrue(validate_user_input(self.user_valid_guess, self.lower_number, self.upper_number))
        self.assertFalse(validate_user_input(user_invalid_range_input, self.lower_number, self.upper_number))
    def test_ckeck_guess(self):
        secret_number = 60
        lower_guess = 50
        upper_guess = 70
        self.assertTrue(check_guess(self.user_valid_guess, secret_number), "Correct")
        self.assertTrue(check_guess(lower_guess, secret_number), "Too low")
        self.assertTrue(check_guess(upper_guess, secret_number), "Too high")

if __name__ == '__main__':
    unittest.main()