def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        input = [[int(c) for c in line] for line in input]
        return input

def find_low_points(input: list) -> list:
    to_check = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    length_rows = len(input)
    length_cols = len(input[0])
    low_points = []
    for row in range(length_rows):
        for col in range(length_cols):
            location = input[row][col]
            neighbours = []
            for neighbour in to_check:
                neighbour_row = neighbour[0]+row
                neighbour_col = neighbour[1]+col
                if 0 <= neighbour_row < length_rows and 0 <= neighbour_col < length_cols:
                    neighbours.append(input[neighbour_row][neighbour_col])
            if all(location < neighbour for neighbour in neighbours):
                low_points.append([row, col])
    return low_points

def part1(input: list) -> int:
    ans = 0
    for low_point in find_low_points(input):
        row, col = low_point
        ans += input[row][col] + 1
    return ans

def paintbucket(row: int, col: int, input: list, visited_points: list) -> int:
    if visited_points[row][col] == 1:
        return 0
    visited_points[row][col] = 1
    to_check = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    length_rows = len(input)
    length_cols = len(input[0])
    for neighbour in to_check:
        neighbour_row = neighbour[0]+row
        neighbour_col = neighbour[1]+col
        if 0 <= neighbour_row < length_rows and 0 <= neighbour_col < length_cols:
            val = input[neighbour_row][neighbour_col]
            if val < 9:
                paintbucket(neighbour_row, neighbour_col, input, visited_points)
    return visited_points

def part2(input: list) -> int:
    ans = 1
    areas = []
    for low_point in find_low_points(input):
        row, col = low_point
        visited_points = [[0 for _ in line] for line in input]
        paintbucket(row, col, input, visited_points)
        areas.append(sum([sum(line) for line in visited_points]))
    areas.sort(reverse = True)
    for i in range(3):
        ans *= areas[i] 
    return ans

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 15
    assert part2(test_input) == 1134

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input))