import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar): 
        return self.__mul__(scalar)
    
    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return self.x == other.x and self.y == other.y
    
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __len__(self):
        return round(self.norm())

print("\n" + "="*50)
print("EXERCISE 2 - Vector2D")
print("="*50)

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {v1 + v2}")
print(f"v1 - v2 = {v1 - v2}")
print(f"v1 * 3 = {v1 * 3}")
print(f"3 * v1 = {3 * v1}")
print(f"v1 == v2 ? {v1 == v2}")
print(f"v1 == Vector2D(3,4) ? {v1 == Vector2D(3, 4)}")
print(f"Norm of v1 = {v1.norm():.2f}")
print(f"Length (__len__) of v1 = {len(v1)}")

print("\nTest __len__ with float return:")

class BadVector(Vector2D):
    def __len__(self):
        return self.norm()  

v3 = BadVector(3, 4)
try:
    print(len(v3))
except TypeError as e:
    print(f"Error: {e}")
