from typing import Tuple
from collections import defaultdict

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        return input

def parse_input(input: list) -> Tuple[list, dict]:
    polymer = input[0]
    polymer_counts = defaultdict(int)
    for i in range(len(polymer)-1):
        polymer_counts[polymer[i]+polymer[i+1]] += 1
    insertion_rules = {}
    for row in input[2:]:
        a, b = row.split(' -> ')
        insertion_rules[a] = b
    return polymer_counts, insertion_rules

def apply_rules(polymer_counts: defaultdict, insertion_rules: dict) -> defaultdict:
    new_counts = defaultdict(int)
    for pair, count in polymer_counts.items():
        rule = insertion_rules[pair]
        new_counts[pair[0] + rule] += count
        new_counts[rule + pair[1]] += count
    return new_counts

def play_game(input: list, steps: int) -> int:
    polymer_counts, insertion_rules = parse_input(input)
    letter_count = defaultdict(int)  
    letter_count[input[0][-1]] += 1 # as last letter of original string is not part of any pairs, it's not included in final count
    for _ in range(steps):
        polymer_counts = apply_rules(polymer_counts, insertion_rules)
    for pair, count in polymer_counts.items():
        letter_count[pair[0]] += count
    ans = max(letter_count.values())- min(letter_count.values())
    return ans

def part1(input: list, steps: int) -> int:
    ans = play_game(input, steps)
    return ans

def part2(input: list, steps: int) -> int:
    ans = play_game(input, steps)
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input, 10) == 1588
    assert part2(test_input, 40) == 2188189693529

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input, 10))
    print(part2(input, 40))