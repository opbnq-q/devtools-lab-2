# math formulas

this project contains functions for calculating the area and perimeter of geometric shapes.

## formulas

### area

- circle: `s = πr²`
- rectangle: `s = ab`
- square: `s = a²`
- triangle: `s = ah / 2`

### perimeter

- circle: `p = 2πr`
- rectangle: `p = 2a + 2b`
- square: `p = 4a`
- triangle: `p = a + b + c`

## functions

## circle

### `area(r)`

calculates the area of a circle.

**arguments:**

- `r` - the radius of the circle. `(float)`

**returns:**

- the area of the circle. `(float)`

**example:**

```python
from circle import area

area(2)
# 12.566370614359172
```

### `perimeter(r)`

calculates the perimeter of a circle.

**arguments:**

- `r` - the radius of the circle. `(float)`

**returns:**

- the perimeter of the circle. `(float)`

**example:**

```python
from circle import perimeter

perimeter(2)
# 12.566370614359172
```

## rectangle

### `area(a, b)`

calculates the area of a rectangle.

**arguments:**

- `a` - the length of the rectangle. `(float)`
- `b` - the width of the rectangle. `(float)`

**returns:**

- the area of the rectangle. `(float)`

**example:**

```python
from rectangle import area

area(2, 3)
# 6
```

### `perimeter(a, b)`

calculates the perimeter of a rectangle.

**arguments:**

- `a` - the length of the rectangle. `(float)`
- `b` - the width of the rectangle. `(float)`

**returns:**

- the perimeter of the rectangle. `(float)`

**example:**

```python
from rectangle import perimeter

perimeter(2, 3)
# 10
```

## square

### `area(a)`

calculates the area of a square.

**arguments:**

- `a` - the side length of the square. `(float)`

**returns:**

- the area of the square. `(float)`

**example:**

```python
from square import area

area(3)
# 9
```

### `perimeter(a)`

calculates the perimeter of a square.

**arguments:**

- `a` - the side length of the square. `(float)`

**returns:**

- the perimeter of the square. `(float)`

**example:**

```python
from square import perimeter

perimeter(3)
# 12
```

## triangle

### `area(a, h)`

calculates the area of a triangle.

**arguments:**

- `a` - the base of the triangle. `(float)`
- `h` - the height of the triangle. `(float)`

**returns:**

- the area of the triangle. `(float)`

**example:**

```python
from triangle import area

area(4, 3)
# 6
```

### `perimeter(a, b, c)`

calculates the perimeter of a triangle.

**arguments:**

- `a` - the first side of the triangle. `(float)`
- `b` - the second side of the triangle. `(float)`
- `c` - the third side of the triangle. `(float)`

**returns:**

- the perimeter of the triangle. `(float)`

**example:**

```python
from triangle import perimeter

perimeter(3, 4, 5)
# 12
```

# project editing history
```bash 
git log --all --graph --oneline
* fe691ba specify project
* e96bfcf fix rectangle && add triangle
* c8b9c9c add rectangle.py
| * 86edb1c L-05: Update Docs. Add user agreement info
| * 438b89a L-05: Add user agreement
| * 6adb962 L-03: Docs added
| | * 3049431 L-04: Add rectangle.py
| |/  
|/|   
| | * b5b0fae L-04: Update docs for calculate.py
| | * d76db2a L-04: Add calculate.py
| | * 51c40eb L-04: Doc updated for triangle
| | * d080c78 L-04: Triangle added
| |/  
|/|   
* | d078c8d L-03: Docs added
|/  
* 8ba9aeb L-03: Circle and square added
```