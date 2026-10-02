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

![image description](./Square%20calculation%20example.jpg)