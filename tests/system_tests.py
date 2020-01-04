import unittest
from src.helpers import load_map_40, load_map_10
from src.route_planner import PathPlanner


class SystemTests(unittest.TestCase):

    map_40 = load_map_40()

    def test_plan_short_path(self):
        planner = PathPlanner(self.map_40, start=5, goal=34)
        path = planner.path
        expected_path = [5, 16, 37, 12, 34]
        self.assertListEqual(path, expected_path, "planner.path is generated a path: %s. Expected path: %s" % (path, expected_path))

    def test_plan_longest_path(self):
        planner = PathPlanner(self.map_40, start=8, goal=24)
        path = planner.path
        expected_path = [8, 14, 16, 37, 12, 17, 10, 24]
        self.assertListEqual(path, expected_path, "planner.path is generated a path: %s. Expected path: %s" % (path, expected_path))

    def test_plan_same_node_path(self):
        planner = PathPlanner(self.map_40, start=4, goal=4)
        path = planner.path
        expected_path = [4]
        self.assertListEqual(path, expected_path, "planner.path is generated a path: %s. Expected path: %s" % (path, expected_path))

    def test_plan_two_nodes_path(self):
        planner = PathPlanner(self.map_40, start=21, goal=19)
        path = planner.path
        expected_path = [21, 19]
        self.assertListEqual(path, expected_path, "planner.path is generated a path: %s. Expected path: %s" % (path, expected_path))

    def test_plan_path_invalid_goal(self):
        goal = -1
        try:
            PathPlanner(self.map_40, start=21, goal=goal)
        except ValueError as e:
            self.assertEquals(str(e),
                              "Must create goal node before running search. " +
                              "Try running PathPlanner.set_goal(start_node)", "Error messages are different")
            return
        self.fail("PathPlanner has generated a path with invalid goal node: %s" % goal)

    def test_plan_path_missing_goal(self):
        planner = PathPlanner(self.map_40, start=14, goal=None)
        path = planner.path
        self.assertIsNone(path, "planner.path is generated a path: %s. Expected path: None" % path)

    def test_plan_path_invalid_start(self):
        start = 40
        try:
            PathPlanner(self.map_40, start=start, goal=3)
        except ValueError as e:
            self.assertEquals(str(e),
                              "Must create start node before running search. " +
                              "Try running PathPlanner.set_start(start_node)", "Error messages are different")
            return
        self.fail("PathPlanner has generated a path with invalid start node: %s" % start)

    def test_plan_path_missing_start(self):
        planner = PathPlanner(self.map_40, start=None, goal=34)
        path = planner.path
        self.assertIsNone(path, "planner.path is generated a path: %s. Expected path: None" % path)

    def test_plan_path_invalid_map(self):
        map_10 = load_map_10()
        try:
            PathPlanner(map_10, start=10, goal=20)
        except ValueError as e:
            self.assertEquals(str(e),
                              "Must create goal node before running search. " +
                              "Try running PathPlanner.set_goal(start_node)", "Error messages are different")
            return
        self.fail("PathPlanner has generated a path with invalid map: %s" % map_10.intersections)

    def test_plan_path_missing_map(self):
        planner = PathPlanner(M=None, start=0, goal=39)
        path = planner.path
        self.assertIsNone(path, "planner.path is generated a path: %s. Expected path: None" % path)
