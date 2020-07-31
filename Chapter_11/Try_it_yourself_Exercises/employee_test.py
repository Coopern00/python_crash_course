# Writing the tests for the Employee Class

import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for employee.py"""

    # Setting up an instance of an empolyee to be used in multiple method tests
    def setUp(self):
        """
        Creates an employee, to be able to use it multiple times for testing.
        """
        self.test_employee = Employee('bob', 'black', annual_salary=45000)

    # This is for testing if it ineed add the default 5000 raise
    def test_give_default(self):
        """Tests the raise giving method with default value."""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.annual_salary, 50000)

    # This is for testing if the custom raise does work
    def test_give_custom_raise(self):
        """Tests the raise giving method with a custom value."""
        self.test_employee.give_raise(15000)
        self.assertEqual(self.test_employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()