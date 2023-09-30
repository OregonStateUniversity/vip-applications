"""
Name: Keshavan Sridhar
OSU Email: sridhake@oregonstate.edu
Date: 9/30/23
Description: Unit tests for custom map function for Vertically Integrated Projects Program

"""
import unittest
from application import map


class TestMap(unittest.TestCase):
    def test_map_outputs(self):
        """Test that the map function outputs correctly"""
        self.assertEqual(
            list(map(lambda x, y, z: (x + y) * z, [2, 4, 5], [7, 8, 9], [1, 2, 4])),
            [9, 24, 56],
        )
        self.assertEqual(
            list(
                map(
                    lambda x, y, z: (x + y) * z,
                    ["a", "b", "c"],
                    ["d", "e", "f"],
                    [4, 5, 2],
                )
            ),
            ["adadadad", "bebebebebe", "cfcf"],
        )
        self.assertEqual(
            list(map(lambda x, y, z: (x + y) * z, [], ["d", "e", "f"], [4, 5, 2])), []
        )

    def test_map_inputs(self):
        """Test invalid map function inputs raise exceptions"""

        with self.assertRaises(TypeError):
            # invalid iterable type tests
            map(lambda x, y, z: (x + y) * z, [2, 4, 5], 1, [1, 2, 4])
            map(lambda x, y, z: (x + y) * z, (2), [7, 8, 9], [1, 2, 4])

            # missing parameter in map function tests
            map(lambda x, y, z: (x + y) * z, [2, 4, 5], [1, 2, 4])
            map(lambda x, y: (x + y), [7, 8, 9])

            # unsupported operand type tests
            map(lambda x, y: (x + y), [3, 4], ["a", 8, 9])
            map(lambda x, y, z: (x + y) * z, [7, 8, 9], [1, 2, 3], ["a", "b", "c"])


if __name__ == "__main__":
    unittest.main()
