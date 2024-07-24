import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'"""

    # test first and last name
    def test_first_last_name(self):
        # call the function to be tested and store the return value that will be tested
        formatted_name = get_formatted_name('jane', 'doe')
        # assert method verifies that the result from the return value matches the expected value
        expected_formatted_fl_name = "Jane Doe"
        self.assertEqual(formatted_name, expected_formatted_fl_name)
        # print(expected_formatted_fl_name)

    # test first, last, and optional middle name
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        expected_formatted_fml_name = "Wolfgang Amadeus Mozart"
        self.assertEqual(formatted_name, expected_formatted_fml_name)
        # print(expected_formatted_fml_name)


if __name__ == '__main__':
    unittest.main()  # runs all tests in the file
