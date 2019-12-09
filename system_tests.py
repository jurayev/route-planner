from helpers import load_map_40
from route_planner import PathPlanner

MAP_40_ANSWERS = [
    (5, 34, [5, 16, 37, 12, 34]),
    (5, 5, [5]),
    (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])
]


def test(shortest_path_function):
    map_40 = load_map_40()
    correct = 0
    for start, goal, answer_path in MAP_40_ANSWERS:
        path = shortest_path_function(map_40, start, goal).path
        if path == answer_path:
            correct += 1
        else:
            print("For start:", start,
                  "Goal:     ", goal,
                  "Your path:", path,
                  "Correct:  ", answer_path)
    if correct == len(MAP_40_ANSWERS):
        print("All tests pass! Congratulations!")
    else:
        print("You passed", correct, "/", len(MAP_40_ANSWERS), "test cases")


def initial_test():
    map_40 = load_map_40()
    planner = PathPlanner(map_40, 5, 34)
    path = planner.path
    if path == [5, 16, 37, 12, 34]:
        print("great! Your code works for these inputs!")
        print(path)
    else:
        print("something is off, your code produced the following:")
        print(path)


initial_test()
test(PathPlanner)
