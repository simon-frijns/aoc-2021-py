from typing import Tuple

def get_input(filename: str) -> list:
    with open(filename) as input:
        input_list = input.read().strip().split("\n")
        return input_list

def parse_commands(commands:list) -> Tuple[int, int, int]:
    horizontal_position = 0
    depth = 0
    aim = 0
    for line in commands:
        command, amount = line.split()
        amount = int(amount)
        match command:
            case 'forward':
                horizontal_position += amount
                depth += aim * amount
            case 'down':
                aim += amount
            case 'up':
                aim -= amount
    return horizontal_position, aim, depth

def part1(commands:list) -> int:
    ans = 0
    # NB: abusing aim == depth between parts 1 and 2 to use parse_commands for both
    horizontal_position, depth, _ = parse_commands(commands)
    ans = horizontal_position * depth
    return ans

def part2(commands: list) -> int:
    ans = 0
    horizontal_position, _, depth = parse_commands(commands)
    ans = horizontal_position * depth
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 150
    assert part2(test_input) == 900

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 