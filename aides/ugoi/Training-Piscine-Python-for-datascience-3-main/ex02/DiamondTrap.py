from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King character, inheriting from Baratheon and Lannister classes."""

    def set_eyes(self, eyes):
        """Set the eye color of the King."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the hair color of the King."""
        self.hairs = hairs

    def get_eyes(self):
        """Return the eye color of the King."""
        return self.eyes

    def get_hairs(self):
        """Return the hair color of the King."""
        return self.hairs
