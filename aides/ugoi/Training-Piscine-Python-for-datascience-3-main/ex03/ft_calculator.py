class calculator:
    """Vector calculator."""

    def __init__(self, vector: list):
        """Initialize calculator with a vector."""
        self.vector = vector

    def __add__(self, scalar) -> None:
        """Add scalar to each element of the vector."""
        self.vector = [i + scalar for i in self.vector]
        print(self.vector)

    def __mul__(self, scalar) -> None:
        """Multiply each element of the vector by a scalar."""
        self.vector = [i * scalar for i in self.vector]
        print(self.vector)

    def __sub__(self, scalar) -> None:
        """Subtract scalar from each element of the vector."""
        self.vector = [i - scalar for i in self.vector]
        print(self.vector)

    def __truediv__(self, scalar) -> None:
        """Divide each element of the vector by a scalar."""
        if scalar == 0:
            print("Error: Division by zero is not allowed.")
            return
        self.vector = [i / scalar for i in self.vector]
        print(self.vector)
