from src.route_planner import PathPlanner
from tests import system_tests, unit_tests


def main():
    unit_test = unit_tests.Tests()
    print("---------RUNNING UNIT TESTS----------------")
    unit_test.create_closedSet_test()
    unit_test.create_openSet_test()
    unit_test.create_cameFrom_test()
    unit_test.create_gScore_test()
    unit_test.create_fScore_test()
    unit_test.set_map_test()
    unit_test.set_start_test()
    unit_test.set_goal_test()
    unit_test.is_open_empty_test()
    unit_test.get_current_node_test()
    unit_test.get_neighbors_test()
    unit_test.get_gScore_test()
    unit_test.distance_test()
    unit_test.get_tentative_gScore_test()
    unit_test.heuristic_cost_estimate_test()
    unit_test.calculate_fScore_test()
    unit_test.record_best_path_to_test()
    print("All Unit tests are passed!")

    system_test = system_tests.Tests()
    print("---------RUNNING SYSTEM TESTS--------------")
    system_test.test_initial()
    system_test.test_full(PathPlanner)


if __name__ == "__main__":
    main()
