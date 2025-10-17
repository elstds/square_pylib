# square_pylib
Python library to calculate square of different figures.

How to add a new Figure
1. Create a new class inheriting from Figure in shapes/shapes.py or a new module.
2. Override area().

### Example:
For a rectangle: 
```python
class Rectangle(Figure): 
    def __init__(self, w, h):
        pass
    def area(self): 
        return self.w * self.h
```
3. Add tests to tests/ directory.
