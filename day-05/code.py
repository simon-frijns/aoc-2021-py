import re

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        return input
    
def create_grid(input: list) -> list:
    c = [col for col in zip(*input)]
    max_x = max(c[0]+c[2]) 
    max_y = max(c[1]+c[3])
    grid = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)] # not too happy about the +1'ing
    return grid

def play_game(input: list, with_diagonals: bool) -> int:
    instructions = []
    for line in input:
        instructions.append(list(map(int, re.findall('\d+', line))))
    grid = create_grid(instructions)
    for instruction in instructions:
        x1, y1, x2, y2 = [value for value in instruction]
        if x1 == x2 or y1 == y2 or with_diagonals:
            sign_x = 1 if x1 < x2 else -1 if x1 > x2 else 0 # can this be cleaner?
            sign_y = 1 if y1 < y2 else -1 if y1 > y2 else 0
            length = max(abs(x1 - x2), abs(y1 - y2))
            for i in range(length + 1):
                x = x1 + sign_x * i
                y = y1 + sign_y * i
                grid[y][x] += 1 
    return sum([sum([point > 1 for point in line]) for line in grid])

def part1(input: list) -> int:
    ans = play_game(input, with_diagonals = False)
    return ans

def part2(input: list) -> int:
    ans = play_game(input, with_diagonals = True)
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 5
    assert part2(test_input) == 12

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 