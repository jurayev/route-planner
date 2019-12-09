from route_planner import PathPlanner
from helpers import load_map_40, load_map_10
import math


def create_closedSet_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    closedSet = planner.create_closedSet()
    assert closedSet == set(), "create_closedSet() function works incorrectly. Expected: set(). Actual: %s " % closedSet


def create_openSet_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    openSet = planner.create_openSet()
    assert openSet == {5}, "create_openSet() function works incorrectly. Expected: {5}. Actual: %s " % openSet


def create_cameFrom_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    cameFrom = planner.create_cameFrom()
    assert cameFrom == {}, "create_cameFrom() function works incorrectly. Expected: {}. Actual: %s " % cameFrom


def create_gScore_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    g_score = planner.create_gScore()
    for score in g_score:
        if score != 5:
            assert g_score[score] == math.inf, "create_gScore() function works incorrectly. Expected: inf. Actual: %s " % g_score[score]
        else:
            assert g_score[5] == 0, "create_gScore() function works incorrectly. Expected: 0. Actual: %s " % g_score[5]


def create_fScore_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 15, 34)
    f_score = planner.create_fScore()
    for score in f_score:
        if score != 15:
            assert f_score[score] == math.inf, "create_f_score() function works incorrectly. Expected: inf. Actual: %s " % f_score[score]
        else:
            assert f_score[15] == 0, "create_f_score() function works incorrectly. Expected: 0. Actual: %s " % f_score[15]


def set_map_test():
    map_10 = load_map_10()
    map_40 = load_map_40()
    planner = PathPlanner(map_10, 7, 3)
    planner.set_map(map_40)
    assert planner.map == map_40, "set_map() function works incorrectly. Expected map: %s. Actual: %s " % (map_40, planner.map)
    assert planner.start == None, "set_map() function works incorrectly. Expected start: %s. Actual: %s " % (None, planner.start)
    assert planner.goal == None, "set_map() function works incorrectly. Expected goal: %s. Actual: %s " % (None, planner.goal)


def set_start_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 37, 14)
    planner.set_start(31)
    assert planner.start == 31, "set_start() function works incorrectly. Expected start: %s. Actual: %s " % (31, planner.start)
    assert planner.goal == None, "set_start() function works incorrectly. Expected goal: %s. Actual: %s " % (None, planner.goal)


def set_goal_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 37, 14)
    planner.set_goal(1)
    assert planner.goal == 1, "set_goal() function works incorrectly. Expected goal: %s. Actual: %s " % (1, planner.goal)


def is_open_empty_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 37, 14)
    assert planner.is_open_empty() == False, "is_open_empty() function works incorrectly. Expected: %s. Actual: %s " % (False, planner.is_open_empty())
    planner.openSet.clear()
    assert planner.is_open_empty() == True, "is_open_empty() function works incorrectly. Expected: %s. Actual: %s " % (True, planner.is_open_empty())


def get_current_node_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 37, 14)
    planner.openSet = {5, 1, 3}
    planner.fScore = {1: 30, 2: 5, 3: 25, 5: 44}
    assert planner.get_current_node() == 3, "get_current_node() function works incorrectly. Expected: %s. Actual: %s " % (3, planner.get_current_node())
    planner.openSet.add(2)
    assert planner.get_current_node() == 2, "get_current_node() function works incorrectly. Expected: %s. Actual: %s " % (2, planner.get_current_node())


def get_neighbors_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    planner.openSet = {32, 16, 14}
    planner.fScore = {32: 10, 16: 5, 14: 7}
    current_node = planner.get_current_node()
    assert planner.get_neighbors(current_node) == [5, 14, 37, 30], "get_neighbors() function works incorrectly. Expected: %s. Actual: %s " % ([5, 14, 37, 30], planner.get_neighbors(current_node))


def get_gScore_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {32: 2, 16: 3, 14: 3}
    assert planner.get_gScore(16) == 3, "get_gScore() function works incorrectly. Expected: %s. Actual: %s " % (3, planner.get_gScore(16))
    assert planner.get_gScore(32) == 2, "get_gScore() function works incorrectly. Expected: %s. Actual: %s " % (2, planner.get_gScore(32))


def distance_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    node_16 = planner.distance(5, 16)
    node_14 = planner.distance(5, 14)
    node_32 = planner.distance(5, 38)
    assert node_16 < node_14 < node_32, "distance() function works incorrectly. Expected: 0.05024121466351104 < 0.14101456789585137 < 0.24522732199439867. Actual: %s < %s < %s" % (node_16, node_14, node_32)


def get_tentative_gScore_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {5: 2, 16: 3, 14: 3}
    tentative_gScore = planner.get_tentative_gScore(5, 16)
    assert tentative_gScore == 2 + 0.05024121466351104, "get_tentative_gScore() function works incorrectly. Expected: 2.05024121466351104. Actual: %s" % tentative_gScore


def heuristic_cost_estimate_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    hScore = planner.heuristic_cost_estimate(5)
    assert hScore == 0.574734871592805, "heuristic_cost_estimate() function works incorrectly. Expected: 0.574734871592805. Actual: %s" % hScore


def calculate_fScore_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {5: 1, 16: 3, 14: 3}
    fScore = planner.calculate_fScore(5)
    assert fScore == 1.574734871592805, "calculate_fScore() function works incorrectly. Expected: 1.574734871592805. Actual: %s" % fScore


def record_best_path_to_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {5: 1, 16: 3, 14: 3}
    planner.record_best_path_to(5, 16)
    assert planner.cameFrom[16] == 5, "record_best_path_to() function works incorrectly. Expected: 5 Actual: %s" % planner.cameFrom[16]
    assert planner.gScore[16] == 1.050241214663511, "record_best_path_to() function works incorrectly. Expected: 1.050241214663511. Actual: %s" % planner.gScore[16]
    assert planner.fScore[16] == 1.57541988984527, "record_best_path_to() function works incorrectly. Expected: 57541988984527. Actual: %s" % planner.fScore[16]
    planner.record_best_path_to(16, 37)
    assert planner.cameFrom[37] == 16, "record_best_path_to() function works incorrectly. Expected: 1.574734871592805. Actual: %s" % planner.cameFrom[37]
    assert planner.gScore[37] == 1.2580230896798086, "record_best_path_to() function works incorrectly. Expected: 1.2580230896798086. Actual: %s" % planner.gScore[37]
    assert planner.fScore[37] == 1.5972660928281592, "record_best_path_to() function works incorrectly. Expected: 1.5972660928281592. Actual: %s" % planner.fScore[37]


create_closedSet_test()
create_openSet_test()
create_cameFrom_test()
create_gScore_test()
create_fScore_test()
set_map_test()
set_start_test()
set_goal_test()
is_open_empty_test()
get_current_node_test()
get_neighbors_test()
get_gScore_test()
distance_test()
get_tentative_gScore_test()
heuristic_cost_estimate_test()
calculate_fScore_test()
record_best_path_to_test()
print("All Unit tests are passed!")

