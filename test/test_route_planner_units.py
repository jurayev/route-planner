"""Tests for route planner units"""
import math
from src.helpers import load_map_10
from src.route_planner import PathPlanner
import pytest


@pytest.mark.unit
def test_create_empty_closed_set(map_40):
    planner = PathPlanner(map_40, 5, 34)
    closed_set = planner.create_closedSet()
    assert set() == closed_set


@pytest.mark.unit
def test_create_open_set_with_start_node(map_40):
    planner = PathPlanner(map_40, 5, 34)
    open_set = planner.create_openSet()
    assert {5} == open_set


@pytest.mark.unit
def test_create_empty_came_from(map_40):
    planner = PathPlanner(map_40, 5, 34)
    came_from = planner.create_cameFrom()
    assert {} == came_from


@pytest.mark.unit
def test_initial_gscore_sets_zero_for_start_node(map_40):
    planner = PathPlanner(map_40, 1, 34)
    g_score = planner.create_gScore()
    assert 0 == g_score[1]


@pytest.mark.unit
def test_initial_gscore_sets_infinity_for_all_except_start_node(map_40):
    planner = PathPlanner(map_40, 2, 39)
    g_score = planner.create_gScore()
    for score in g_score:
        if score != 2:
            assert g_score[score] == math.inf


@pytest.mark.unit
def test_initial_fscore_sets_zero_for_start_node(map_40):
    planner = PathPlanner(map_40, 3, 11)
    f_score = planner.create_fScore()
    assert 0 == f_score[3]


@pytest.mark.unit
def test_initial_fscore_sets_infinity_for_all_except_start_node(map_40):
    planner = PathPlanner(map_40, 1, 39)
    f_score = planner.create_fScore()
    for score in f_score:
        if score != 1:
            assert f_score[score] == math.inf


@pytest.mark.unit
def test_set_new_map(map_40):
    planner = PathPlanner(load_map_10(), 7, 3)
    planner.set_map(map_40)
    assert map_40 == planner.map
    assert planner.start is None
    assert planner.goal is None


@pytest.mark.unit
def test_set_new_start(map_40):
    planner = PathPlanner(map_40, 37, 14)
    new_start = 31
    planner.set_start(new_start)
    assert new_start == planner.start
    assert planner.goal is None


@pytest.mark.unit
def test_set_new_goal(map_40):
    planner = PathPlanner(map_40, 15, 25)
    new_goal = 1
    planner.set_goal(new_goal)
    assert new_goal == planner.goal


@pytest.mark.unit
def test_open_set_is_not_empty(map_40):
    planner = PathPlanner(map_40, 37, 14)
    assert not planner.is_open_empty()


@pytest.mark.unit
def test_open_set_is_empty(map_40):
    planner = PathPlanner(map_40, 37, 14)
    planner.openSet.clear()
    assert planner.is_open_empty()


@pytest.mark.unit
def test_get_current_node(map_40):
    planner = PathPlanner(map_40, 14, 14)
    lowest_value = 3
    planner.openSet = {5, 1, lowest_value}
    planner.fScore = {1: 30, 2: 5, 3: 25, 5: 44}
    assert planner.get_current_node() == lowest_value


@pytest.mark.unit
def test_get_neighbors_for_current_node(map_40):
    planner = PathPlanner(map_40, 5, 34)
    planner.openSet = {32, 16, 14}
    planner.fScore = {32: 10, 16: 5, 14: 7}
    expected_neighbors = [5, 14, 37, 30]
    current_node = planner.get_current_node()
    neighbors = planner.get_neighbors(current_node)
    assert expected_neighbors == neighbors


@pytest.mark.unit
def test_get_gscore(map_40):
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {32: 2, 16: 3, 14: 3}
    gscore = planner.get_gScore(16)
    assert 3 == gscore


@pytest.mark.unit
def test_distance_computation(map_40):
    planner = PathPlanner(map_40, 5, 34)
    node_16_closest = planner.distance(5, 16)
    node_14_mid_range = planner.distance(5, 14)
    node_38_farthest = planner.distance(5, 38)
    assert node_16_closest < node_14_mid_range < node_38_farthest


@pytest.mark.unit
def test_get_tentative_gscore(map_40):
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {5: 2, 16: 3, 14: 3}
    tentative_gscore = planner.get_tentative_gScore(5, 16)
    assert 2.05024121466351104 == tentative_gscore


@pytest.mark.unit
def test_heuristic_cost_estimate(map_40):
    planner = PathPlanner(map_40, 5, 34)
    h_score = planner.heuristic_cost_estimate(5)
    assert 0.574734871592805 == h_score


@pytest.mark.unit
def test_calculate_fscore(map_40):
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {5: 1, 16: 3, 14: 3}
    f_score = planner.calculate_fScore(5)
    assert 1.574734871592805 == f_score


@pytest.mark.unit
def test_record_best_path(map_40):
    planner = PathPlanner(map_40, 5, 34)
    planner.gScore = {5: 1, 16: 3, 14: 3}
    current_node = 5
    neighbor_node = 16
    planner.record_best_path_to(current_node, neighbor_node)
    came_from_node = planner.cameFrom[neighbor_node]
    g_score = planner.gScore[neighbor_node]
    f_score = planner.fScore[neighbor_node]
    assert current_node == came_from_node
    assert 1.050241214663511 == g_score
    assert 1.57541988984527 == f_score


@pytest.mark.unit
def test_plan_path_with_invalid_goal(map_40):
    invalid_goal = -1
    with pytest.raises(ValueError, match=r".*goal node.*"):
        PathPlanner(map_40, start=21, goal=invalid_goal)


@pytest.mark.unit
def test_plan_path_with_invalid_start(map_40):
    invalid_start = 40
    with pytest.raises(ValueError, match=r".*start node.*"):
        PathPlanner(map_40, start=invalid_start, goal=21)


@pytest.mark.unit
def test_plan_path_with_missing_goal_on_map_10():
    map_10 = load_map_10()
    with pytest.raises(ValueError, match=r".*goal node.*"):
        PathPlanner(map_10, start=10, goal=20)
