# Class: blueprint for creating new objects

# Class: Human
# Objects: John, Mary, Mark

class Point:
    # Class Level Attribute
    default_color = "red"

    # Constructor
    def __init__(self, x: int, y: int):
        # Instance Attributes
        self.x = x
        self.y = y

    # Magic Methods
    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Instance Method
    def draw(self):
        print(f"Point {self.x} {self.y}")

    # Class Method
    @classmethod
    def zero(cls):
        return cls(0, 0)


origin = Point.zero()
point = Point(1, 2)
point.draw()
print(point.default_color, Point.default_color)
print(type(point))
print(isinstance(point, Point))
