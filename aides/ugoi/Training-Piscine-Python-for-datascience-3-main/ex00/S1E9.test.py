import unittest
from S1E9 import Character, Stark

class TestStark(unittest.TestCase):

    def test_stark_initialization(self):
        Ned = Stark("Ned")
        self.assertEqual(Ned.first_name, "Ned")
        self.assertTrue(Ned.is_alive)
        
    def test_stark_death(self):
        Ned = Stark("Ned")
        Ned.die()
        self.assertFalse(Ned.is_alive)

    def test_stark_initialization_with_is_alive_false(self):
        Lyanna = Stark("Lyanna", False)
        self.assertEqual(Lyanna.first_name, "Lyanna")
        self.assertFalse(Lyanna.is_alive)

    def test_docstrings(self):
        Ned = Stark("Ned")
        self.assertIsNotNone(Ned.__doc__)
        self.assertIsNotNone(Ned.__init__.__doc__)
        self.assertIsNotNone(Ned.die.__doc__)

if __name__ == "__main__":
    unittest.main()
