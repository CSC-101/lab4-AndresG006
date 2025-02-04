import lab4
import unittest

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)


        # write a second test here

    def test_first_element_2(self):
        input = [[1, 2], [3, 4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    # Part 2
    import unittest

    class TestXCoordinates(unittest.TestCase):

        def test_x_coordinates_1(self):
            points = [lab4.Point(1, 2), lab4.Point(3, 4), lab4.Point(5, 6)]
            result = lab4.x_coordinates(points)
            expected = [1, 3, 5]
            self.assertEqual(expected, result)

        def test_x_coordinates_2(self):
            points = [lab4.Point(7, 8), lab4.Point(0, 0), lab4.Point(-5, 10)]
            result = lab4.x_coordinates(points)
            expected = [7, 0, -5]
            self.assertEqual(expected, result)

    # Part 3
    import unittest
    class TestAreInPositiveQuadrant(unittest.TestCase):

        def test_are_in_positive_quadrant_1(self):
            points = [lab4.Point(1, 2), lab4.Point(-3, 4), lab4.Point(5, -6), lab4.Point(7, 8)]
            result = lab4.are_in_positive_quadrant(points)
            expected = [lab4.Point(1, 2), lab4.Point(7, 8)]
            self.assertEqual([point.x for point in result], [point.x for point in expected])
            self.assertEqual([point.y for point in result], [point.y for point in expected])

        def test_are_in_positive_quadrant_2(self):
            points = [lab4.Point(1, 2), lab4.Point(-1, -2), lab4.Point(0, 1), lab4.Point(2, 3)]
            result = lab4.are_in_positive_quadrant(points)
            expected = [lab4.Point(1, 2), lab4.Point(2, 3)]
            self.assertEqual([point.x for point in result], [point.x for point in expected])
            self.assertEqual([point.y for point in result], [point.y for point in expected])

    # Part 4
    import unittest
    class TestDistance(unittest.TestCase):
        def test_distance_1(self):
            point1 = lab4.Point(0, 0)
            point2 = lab4.Point(3, 4)
            result = lab4.distance(point1, point2)
            expected = 5.0
            tolerance = 1e-9  # Tolerance for floating-point comparison
            self.assertAlmostEqual(result, expected, delta=tolerance)

        def test_distance_2(self):
            point1 = lab4.Point(1, 1)
            point2 = lab4.Point(4, 5)
            result = lab4.distance(point1, point2)
            expected = 5.0
            tolerance = 1e-9  # Tolerance for floating-point comparison
            self.assertAlmostEqual(result, expected, delta=tolerance)
    # Part 5
    import unittest
    class TestManhattanDistance(unittest.TestCase):

        def test_manhattan_distance_1(self):
            point1 = lab4.Point(1, 2)
            point2 = lab4.Point(4, 6)
            result = lab4.manhattan_distance(point1, point2)
            expected = 7.0  # |4 - 1| + |6 - 2| = 3 + 4 = 7
            tolerance = 1e-9  # Tolerance for floating-point comparison
            self.assertAlmostEqual(result, expected, delta=tolerance)

        def test_manhattan_distance_2(self):
            point1 = lab4.Point(-1, -1)
            point2 = lab4.Point(2, 3)
            result = lab4.manhattan_distance(point1, point2)
            expected = 7.0  # |2 - (-1)| + |3 - (-1)| = 3 + 4 = 7
            tolerance = 1e-9  # Tolerance for floating-point comparison
            self.assertAlmostEqual(result, expected, delta=tolerance)

    # Part 6
import unittest
class TestDistanceAll(unittest.TestCase):

    def test_distance_all_1(self):
        points = [lab4.Point(3, 4), lab4.Point(1, 1), lab4.Point(0, 5)]
        result = lab4.distance_all(points)
        expected = [5.0, 1.4142135623730951, 5.0]
        tolerance = 1e-9
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=tolerance)

    def test_distance_all_2(self):
        points = [lab4.Point(-1, -1), lab4.Point(2, 3), lab4.Point(4, 5)]
        result = lab4.distance_all(points)
        expected = [1.4142135623730951, 3.605551275463989, 6.4031242374328485]
        tolerance = 1e-9
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, delta=tolerance)




if __name__ == '__main__':
    unittest.main()
