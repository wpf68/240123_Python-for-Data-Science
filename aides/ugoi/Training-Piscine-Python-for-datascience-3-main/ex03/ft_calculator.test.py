import unittest
from ft_calculator import calculator
from unittest.mock import patch
from io import StringIO

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()
        self.patcher = patch('sys.stdout', self.held_output)
        self.patcher.start()

    def tearDown(self):
        self.held_output.close()
        self.patcher.stop()

    def test_addition(self):
        v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        self.assertEqual(self.held_output.getvalue().strip(), "[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]")
        self.held_output.truncate(0)  # Clear the output buffer
        self.held_output.seek(0)      # Reset the buffer's cursor to the start

    def test_multiplication(self):
        v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        self.assertEqual(self.held_output.getvalue().strip(), "[0.0, 5.0, 10.0, 15.0, 20.0, 25.0]")
        self.held_output.truncate(0)
        self.held_output.seek(0)

    def test_subtraction_and_division(self):
        v3 = calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5
        self.assertEqual(self.held_output.getvalue().strip(), "[5.0, 10.0, 15.0]\n[1.0, 2.0, 3.0]")
        self.held_output.truncate(0)
        self.held_output.seek(0)

if __name__ == '__main__':
    unittest.main()
