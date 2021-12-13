from typing import Tuple
import re

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read()
        return input

def parse_input(input: list) -> Tuple[list, list]:
    points, instructions = input.split("\n\n")
    points = [point for point in points.split('\n')]
    coordset = set()
    for point in points:
        coordset.add(tuple(map(int, re.findall('\d+', point))))
    folds = []
    for line in instructions.split('\n'):
        axis = re.findall('(x|y)', line)[0]
        fold_line = int(re.findall('\d+', line)[0])
        folds.append([axis, fold_line])
    return coordset, folds

def do_fold(coordset: set, fold: list) -> list:
    axis, fold_line = fold
    new_coordset = set()
    for x, y in coordset:
        if axis == 'x' and x > fold_line:
            x = fold_line - (x - fold_line)
        if axis == 'y' and y > fold_line:
            y = fold_line - (y - fold_line)
        new_coordset.add(tuple([x, y]))
    return new_coordset

def part1(input: list) -> int:
    ans = 0
    coordset, folds = parse_input(input)
    fold = folds[0]
    new_grid = do_fold(coordset, fold)
    ans = len(new_grid)
    return ans

def part2(input: list):
    coordset, folds = parse_input(input)
    fold = folds[0]
    new_coordset = do_fold(coordset, fold)
    for fold in folds:
        new_coordset = do_fold(new_coordset, fold)
    max_x = max([x for x, _ in new_coordset]) + 1
    max_y = max([y for _, y in new_coordset]) + 1
    ans_grid = [['⬛' for _ in range(max_x)] for _ in range(max_y)]
    for x in range(max_x):
        for y in range(max_y):
            if (x, y) in new_coordset:
                ans_grid[y][x] = '🟩'
    for row in ans_grid:
        print(''.join(row))
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 17
    # yeaaaah about that testing

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    part2(input)