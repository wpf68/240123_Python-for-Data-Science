from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for a character."""
    def __init__(self,  first_name, is_alive=True):
        """Initialize with first name and alive status (default: True)."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to simulate character's death."""
        ...


class Stark(Character):
    """Class for a Stark family member."""
    def die(self):
        """Simulate Stark character's death by marking as not alive."""
        self.is_alive = False
