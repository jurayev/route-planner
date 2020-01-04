import math
import unittest
from src.route_planner import PathPlanner
from src.helpers import load_map_40, load_map_10


class UnitTests(unittest.TestCase):

    map_40 = load_map_40()

    def test_create_closedSet(self):
        planner = PathPlanner(self.map_40, 5, 34)
        closed_set = planner.create_closedSet()
        expected_closed_set = set()
        self.assertSetEqual(closed_set, expected_closed_set, "create_closedSet() works incorrectly. Expected: set(). Actual: %s " % closed_set)

    def test_create_openSet(self):
        planner = PathPlanner(self.map_40, 5, 34)
        open_set = planner.create_openSet()
        expected_frontier = {5}
        self.assertSetEqual(open_set, expected_frontier, "create_closedSet() works incorrectly. Expected: set(). Actual: %s " % open_set)

    def test_create_cameFrom(self):
        planner = PathPlanner(self.map_40, 5, 34)
        came_from = planner.create_cameFrom()
        self.assertDictEqual(came_from, {}, "create_cameFrom() works incorrectly. Expected: {}. Actual: %s " % came_from)

    def test_create_gScore(self):
        planner = PathPlanner(self.map_40, 5, 34)
        g_score = planner.create_gScore()
        for score in g_score:
            if score != 5:
                self.assertEquals(g_score[score], math.inf, "create_gScore() works incorrectly. Expected: inf. Actual: %s " % g_score[score])
            else:
                self.assertEquals(g_score[5], 0, "create_gScore() works incorrectly. Expected: 0. Actual: %s " % g_score[5])

    def test_create_fScore(self):
        planner = PathPlanner(self.map_40, 15, 34)
        f_score = planner.create_fScore()
        for score in f_score:
            if score != 15:
                self.assertEquals(f_score[score], math.inf, "create_f_score() works incorrectly. Expected: inf. Actual: %s " % f_score[score])
            else:
                self.assertEquals(f_score[15], 0, "create_f_score() works incorrectly. Expected: 0. Actual: %s " % f_score[15])

    def test_set_map(self):
        map_10 = load_map_10()
        planner = PathPlanner(map_10, 7, 3)
        planner.set_map(self.map_40)
        self.assertEquals(planner.map, self.map_40, "set_map() works incorrectly. Expected map: %s. Actual: %s " % (self.map_40, planner.map))
        self.assertIsNone(planner.start, "set_map() works incorrectly. Expected start: None. Actual: %s " % planner.start)
        self.assertIsNone(planner.goal, "set_map() works incorrectly. Expected goal: None. Actual: %s " % planner.goal)

    def test_set_start(self):
        planner = PathPlanner(self.map_40, 37, 14)
        start = 31
        planner.set_start(start)
        self.assertEquals(planner.start, start, "set_start() works incorrectly. Expected start: %s. Actual: %s " % (start, planner.start))
        self.assertIsNone(planner.goal, "set_start() works incorrectly. Expected goal: None. Actual: %s " % planner.goal)

    def test_set_goal(self):
        planner = PathPlanner(self.map_40, 15, 25)
        goal = 1
        planner.set_goal(goal)
        self.assertEquals(planner.goal, goal, "set_goal() works incorrectly. Expected: %s. Actual: %s " % (goal, planner.goal))

    def test_is_open_empty(self):
        planner = PathPlanner(self.map_40, 37, 14)
        should_not_be_empty = planner.is_open_empty()
        self.assertFalse(should_not_be_empty, "is_open_empty() works incorrectly. Expected: False. Actual: %s " % should_not_be_empty)
        planner.openSet.clear()
        should_be_empty = planner.is_open_empty()
        self.assertTrue(should_be_empty, "is_open_empty() works incorrectly. Expected: True. Actual: %s " % should_be_empty)

    def test_get_current_node(self):
        planner = PathPlanner(self.map_40, 37, 14)
        lowest = 3
        planner.openSet = {5, 1, lowest}
        planner.fScore = {1: 30, 2: 5, 3: 25, 5: 44}
        current_node = planner.get_current_node()
        self.assertEquals(current_node, lowest, "get_current_node() works incorrectly. Expected: %s. Actual: %s " % (lowest, current_node))
        new_lowest = 2
        planner.openSet.add(new_lowest)
        new_current_node = planner.get_current_node()
        self.assertEquals(new_current_node, new_lowest, "get_current_node() works incorrectly. Expected: %s. Actual: %s " % (new_lowest, new_current_node))

    def test_get_neighbors(self):
        planner = PathPlanner(self.map_40, 5, 34)
        planner.openSet = {32, 16, 14}
        planner.fScore = {32: 10, 16: 5, 14: 7}
        current_node = planner.get_current_node()
        neighbors = planner.get_neighbors(current_node)
        expected_neighbors = [5, 14, 37, 30]
        self.assertListEqual(neighbors, expected_neighbors, "get_neighbors() works incorrectly. Expected: %s. Actual: %s " % (expected_neighbors, neighbors))

    def test_get_gScore(self):
        planner = PathPlanner(self.map_40, 5, 34)
        planner.gScore = {32: 2, 16: 3, 14: 3}
        expected_gscore = 3
        gscore = planner.get_gScore(16)
        self.assertEquals(gscore, expected_gscore, "get_gScore() works incorrectly. Expected: %s. Actual: %s " % (expected_gscore, gscore))
        expected_gscore_two = 2
        gscore_two = planner.get_gScore(32)
        self.assertEquals(gscore_two, expected_gscore_two, "get_gScore() works incorrectly. Expected: %s. Actual: %s " % (expected_gscore_two, gscore_two))

    def test_distance(self):
        planner = PathPlanner(self.map_40, 5, 34)
        node_16 = planner.distance(5, 16)
        node_14 = planner.distance(5, 14)
        node_32 = planner.distance(5, 38)
        self.assertTrue(node_16 < node_14 < node_32, "distance() works incorrectly. Expected: 0.05024121466351104 < 0.14101456789585137 < 0.24522732199439867. Actual: %s < %s < %s" % (node_16, node_14, node_32))

    def test_get_tentative_gScore(self):
        planner = PathPlanner(self.map_40, 5, 34)
        planner.gScore = {5: 2, 16: 3, 14: 3}
        tentative_gscore = planner.get_tentative_gScore(5, 16)
        self.assertEquals(tentative_gscore, 2.05024121466351104, "get_tentative_gScore() works incorrectly. Expected: 2.05024121466351104. Actual: %s" % tentative_gscore)

    def test_heuristic_cost_estimate(self):
        planner = PathPlanner(self.map_40, 5, 34)
        h_score = planner.heuristic_cost_estimate(5)
        self.assertEquals(h_score, 0.574734871592805, "heuristic_cost_estimate() works incorrectly. Expected: 0.574734871592805. Actual: %s" % h_score)

    def test_calculate_fScore(self):
        planner = PathPlanner(self.map_40, 5, 34)
        planner.gScore = {5: 1, 16: 3, 14: 3}
        f_score = planner.calculate_fScore(5)
        self.assertEquals(f_score, 1.574734871592805, "calculate_fScore() works incorrectly. Expected: 1.574734871592805. Actual: %s" % f_score)

    def test_record_best_path(self):
        planner = PathPlanner(self.map_40, 5, 34)
        planner.gScore = {5: 1, 16: 3, 14: 3}
        current_one = 5
        neighbor_one = 16
        planner.record_best_path_to(current_one, neighbor_one)
        came_from_one = planner.cameFrom[neighbor_one]
        g_score_one = planner.gScore[neighbor_one]
        f_score_one = planner.fScore[neighbor_one]
        self.assertEquals(came_from_one, current_one, "record_best_path_to() works incorrectly. Expected: %s. Actual: %s" % (current_one, came_from_one))
        self.assertEquals(g_score_one, 1.050241214663511, "record_best_path_to() works incorrectly. Expected: 1.050241214663511. Actual: %s" % g_score_one)
        self.assertEquals(f_score_one, 1.57541988984527, "record_best_path_to() works incorrectly. Expected: 57541988984527. Actual: %s" % f_score_one)
        # now current node: 16 has g score of 1.050241214663511
        # and current node: 16 has f score of 1.57541988984527
        # so I will use for the robust test
        planner.record_best_path_to(16, 37)
        current_two = 16
        neighbor_two = 37
        planner.record_best_path_to(current_two, neighbor_two)
        came_from_two = planner.cameFrom[neighbor_two]
        g_score_two = planner.gScore[neighbor_two]
        f_score_two = planner.fScore[neighbor_two]
        self.assertEquals(came_from_two, current_two, "record_best_path_to() works incorrectly. Expected: %s. Actual: %s" % (current_two, came_from_two))
        self.assertEquals(g_score_two, 1.2580230896798086, "record_best_path_to() works incorrectly. Expected: 1.2580230896798086. Actual: %s" % g_score_two)
        self.assertEquals(f_score_two, 1.5972660928281592, "record_best_path_to() works incorrectly. Expected: 1.5972660928281592. Actual: %s" % f_score_two)
