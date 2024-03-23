import unittest
from io import StringIO
import sys
from ft_calculator import calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        # Capture the printed output using StringIO
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset the standard output
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def test_calculations(self):
        a = [5, 10, 2]
        b = [2, 4, 3]

        calculator.dotproduct(a, b)
        calculator.add_vec(a, b)
        calculator.sous_vec(a, b)

        # Retrieve the captured output
        self.held_output.seek(0)
        output = self.held_output.read().strip().split('\n')
        
        # Check the output
        self.assertEqual(output[0], "Dot product is: 56")
        self.assertEqual(output[1], "Add Vector is : [7.0, 14.0, 5.0]")
        self.assertEqual(output[2], "Sous Vector is: [3.0, 6.0, -1.0]")

if __name__ == '__main__':
    unittest.main()
