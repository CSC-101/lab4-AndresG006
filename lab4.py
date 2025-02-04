

# Write your functions for each part in the space below.

# Part 1
def first_element(lst: list[list[int]]) -> list[int]:
    non_empty_lists = filter(lambda x: len(x) > 0, lst)

    return [sublist[0] for sublist in non_empty_lists]

# Part 2
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def x_coordinates(points: list[Point]) -> list[int]:
    return list(map(lambda point: point.x, points))

# Part 3
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def are_in_positive_quadrant(points: list[Point]) -> list[Point]:
    return list(filter(lambda point: point.x > 0 and point.y > 0, points))

# Part 4
import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def distance(point1: Point, point2: Point) -> float:
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

# Part 5
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def manhattan_distance(point1: Point, point2: Point) -> float:
    return abs(point2.x - point1.x) + abs(point2.y - point1.y)

#Part 6

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

def distance_(point1: Point, point2: Point) -> float:
    return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)

def distance_all(points: list[Point]) -> list[float]:
    origin = Point(0, 0)
    return list(map(lambda point: distance(origin, point), points))
