to_check = []
for i in range(-1, 2):
    for j in range(-1, 2):
        to_check.append([i, j])

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        input = [[int(c) for c in line] for line in input]
        return input
                   
def play_game(octopi: list, length_rows: int, length_cols: int, steps: int):
    flashes = 0
    end_step = None
    for step in range(steps):
        number_of_0s = 0
        for row in range(length_rows):
            for col in range(length_cols):
                if octopi[row][col] == 0:
                    number_of_0s += 1
        if number_of_0s == length_cols * length_rows and not end_step:
            end_step = step
        for row in range(length_rows):
            for col in range(length_cols):
                octopi[row][col] += 1
        while max(map(max, octopi)) >= 10:
            for row in range(length_rows):
                for col in range(length_cols):
                    if octopi[row][col] >= 10:
                        octopi[row][col] = 0
                        flashes += 1
                        for neighbour in to_check:
                            neighbour_row = neighbour[0] + row
                            neighbour_col = neighbour[1] + col
                            if 0 <= neighbour_row < length_rows and 0 <= neighbour_col < length_cols:
                                if 0 < octopi[neighbour_row][neighbour_col] < 10:
                                    octopi[neighbour_row][neighbour_col] += 1
    return flashes, end_step

def part1(octopi: list) -> int:
    length_rows = len(octopi)
    length_cols = len(octopi[0])
    ans, _ = play_game(octopi, length_rows, length_cols, 100)
    return ans

def part2(input: list) -> int:
    length_rows = len(input)
    length_cols = len(input[0])
    _, ans = play_game(input, length_rows, length_cols, 500)
    return ans
    
def test():
    test_in_p1 = get_input("test_input.txt")
    test_in_p2 = get_input("test_input.txt")
    assert part1(test_in_p1) == 1656
    assert part2(test_in_p2) == 195

if __name__ == "__main__":
    test()
    input_p1 = get_input("input.txt")
    input_p2 = get_input("input.txt")
    print(part1(input_p1))
    print(part2(input_p2)) 