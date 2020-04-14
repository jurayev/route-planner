"""Tests for route planner full functionality"""
from src.route_planner import PathPlanner
import pytest


@pytest.mark.system
@pytest.mark.smoke
@pytest.mark.parametrize("start, goal, expected_path",
                         [(5, 34, [5, 16, 37, 12, 34]),              # short path scenario
                          (8, 24, [8, 14, 16, 37, 12, 17, 10, 24]),  # the longest path scenario
                          (4, 4, [4]),                               # the same node path scenario
                          (21, 19, [21, 19])                         # two nodes path scenario
                         ])
def test_plan_path(map_40, start, goal, expected_path):
    planner = PathPlanner(map_40, start, goal)
    assert expected_path == planner.path


@pytest.mark.system
@pytest.mark.parametrize("start, goal",
                         [(14, None),
                          (None, 34)
                         ])
def test_plan_path_with_missing_start_or_goal(map_40, start, goal):
    planner = PathPlanner(map_40, start=start, goal=goal)
    assert planner.path is None


@pytest.mark.system
def test_plan_path_with_missing_map():
    planner = PathPlanner(M=None, start=0, goal=39)
    assert planner.path is None
