import unittest

from rc_robots_solution import solve_rc_robots

class TestRCRobots(unittest.TestCase):
    def test_basic_movement(self):
        input_data = "5 5\n1 2 N\nLMLMLMLMM"
        expected_output = "1 3 N"
        self.assertEqual(solve_rc_robots(input_data), expected_output)

    def test_turning_and_moving(self):
        input_data = "5 5\n3 3 E\nMMRMMRMRRM"
        expected_output = "5 1 E"
        self.assertEqual(solve_rc_robots(input_data), expected_output)

    def test_multiple_robots(self):
        input_data = "5 5\n1 0 N\nMMRMMLMMR\n3 2 E\nMLLMMRMM"
        expected_output = "3 4 E\n2 4 N"
        self.assertEqual(solve_rc_robots(input_data), expected_output)

    def test_robot_at_boundary(self):
        input_data = "5 5\n0 0 W\nMMMM"
        expected_output = "0 0 W"
        self.assertEqual(solve_rc_robots(input_data), expected_output)

    def test_no_movement_commands(self):
        input_data = "5 5\n2 2 S\nR"
        expected_output = "2 2 W"
        self.assertEqual(solve_rc_robots(input_data), expected_output)

    def test_edge_of_grid_handling(self):
        input_data = "5 5\n5 5 N\nMM\n0 0 S\nMM"
        expected_output = "5 5 N\n0 0 S"
        self.assertEqual(solve_rc_robots(input_data), expected_output)


if __name__ == '__main__':
    unittest.main()