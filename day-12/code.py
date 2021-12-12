from collections import defaultdict
from copy import deepcopy

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        return input

def go_through(point: str, already_visited: set, connected_points: dict) -> int:
    if point == 'start' and already_visited: 
        return 0
    if point == 'end': 
        return 1
    if point.islower() and point in already_visited:
        return 0
    if point.islower():
        already_visited = deepcopy(already_visited)
        already_visited.add(point)
    num_paths = 0
    for point in connected_points[point]:
        num_paths += go_through(point, already_visited, connected_points)
    return num_paths

def go_through_p2(point: str, already_visited: set, connected_points: dict, twice_cave: str) -> int:
    if point == 'start' and already_visited: 
        return 0
    if point == 'end':
        return 1
    if point.islower() and point in already_visited:
        if twice_cave:
            return 0
        else:
            twice_cave = point
    if point.islower():
        already_visited = deepcopy(already_visited)
        already_visited.add(point)
    num_paths = 0
    for point in connected_points[point]:
        num_paths += go_through_p2(point, already_visited, connected_points, twice_cave)
    return num_paths

def part1(input: list) -> int:
    connected_points = defaultdict(list)
    for i in input:
        a,b = i.strip().split('-')
        connected_points[a].append(b) 
        connected_points[b].append(a)
    already_visited = set()
    ans = go_through('start', already_visited, connected_points) 
    return ans

def part2(input: list) -> int:
    connected_points = defaultdict(list)
    for i in input:
        a,b = i.strip().split('-')
        connected_points[a].append(b) 
        connected_points[b].append(a)
    already_visited = set()
    twice_cave = None
    ans = go_through_p2('start', already_visited, connected_points, twice_cave) 
    return ans
    
def test():
    test_input = get_input("test_input_1.txt")
    assert part1(test_input) == 10
    assert part2(test_input) == 36
    test_input = get_input("test_input_2.txt")
    assert part1(test_input) == 19
    assert part2(test_input) == 103
    test_input = get_input("test_input_3.txt")
    assert part1(test_input) == 226
    assert part2(test_input) == 3509

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 