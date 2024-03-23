import unittest
from DiamondTrap import King

class TestKing(unittest.TestCase):

    def setUp(self):
        self.Joffrey = King("Joffrey")

    def test_king_initialization(self):
        self.assertEqual(self.Joffrey.__dict__, 
                         {'first_name': 'Joffrey', 
                          'is_alive': True, 
                          'family_name': 'Baratheon', 
                          'eyes': 'brown', 
                          'hairs': 'dark'})

    def test_set_eyes(self):
        self.Joffrey.set_eyes("blue")
        self.assertEqual(self.Joffrey.get_eyes(), "blue")

    def test_set_hairs(self):
        self.Joffrey.set_hairs("light")
        self.assertEqual(self.Joffrey.get_hairs(), "light")

    def test_updated_king_attributes(self):
        self.Joffrey.set_eyes("blue")
        self.Joffrey.set_hairs("light")
        self.assertEqual(self.Joffrey.__dict__, 
                         {'first_name': 'Joffrey', 
                          'is_alive': True, 
                          'family_name': 'Baratheon', 
                          'eyes': 'blue', 
                          'hairs': 'light'})

if __name__ == '__main__':
    unittest.main()
