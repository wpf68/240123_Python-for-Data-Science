# tester.py

import unittest
from S1E7 import Baratheon, Lannister

class TestCharacters(unittest.TestCase):

    def test_baratheon(self):
        Robert = Baratheon("Robert")
        self.assertEqual(Robert.__dict__, {'first_name': 'Robert', 'is_alive': True, 'family_name': 'Baratheon', 'eyes': 'brown', 'hairs': 'dark'})
        self.assertEqual(str(Robert), "Vector: ('Baratheon', 'brown', 'dark')")
        self.assertEqual(repr(Robert), "Vector: ('Baratheon', 'brown', 'dark')")
        self.assertTrue(Robert.is_alive)
        Robert.die()
        self.assertFalse(Robert.is_alive)
        self.assertEqual(Robert.__doc__, "Representing the Baratheon family.")

    def test_lannister(self):
        Cersei = Lannister("Cersei")
        self.assertEqual(Cersei.__dict__, {'first_name': 'Cersei', 'is_alive': True, 'family_name': 'Lannister', 'eyes': 'blue', 'hairs': 'light'})
        self.assertEqual(str(Cersei), "Vector: ('Lannister', 'blue', 'light')")
        self.assertTrue(Cersei.is_alive)
        
        Jaine = Lannister.create_lannister("Jaine", True)
        self.assertEqual(Jaine.first_name, "Jaine")
        self.assertEqual(type(Jaine).__name__, "Lannister")
        self.assertTrue(Jaine.is_alive)

if __name__ == '__main__':
    unittest.main()
