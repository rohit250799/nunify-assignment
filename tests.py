import unittest

from rc_robots_solution import solve_rc_robots

class TestRCRobots(unittest.TestCase):
    def test_basic_movement(self):
        input_data = "5 5\n1 2 N\nLMLMLMLMM"
        expected_output = "1 3 N"
        self.assertEqual(solve_rc_robots(input_data), expected_output)



if __name__ == '__main__':
    unittest.main()