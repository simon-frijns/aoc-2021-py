from typing import Tuple

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        return input

matching_characters = [
    (')', '('),
    (']', '['),
    ('}', '{'),
    ('>', '<')
]
closing_brackets = [pair[0] for pair in matching_characters]
opening_brackets = [pair[1] for pair in matching_characters]

syntax_error_score = { 
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def part1(input: list) -> int:
    ans = 0
    for chunk in input:
        to_resolve = []
        for c in chunk:
            if c in closing_brackets: 
                matching_character = opening_brackets[closing_brackets.index(c)]
            if c in opening_brackets: 
                to_resolve.append(c)
            else:
                if to_resolve.pop() != matching_character:
                    ans += syntax_error_score[c]
                    break
    return ans

def part2(input: list) -> int:
    ans = 0
    error_scores = []
    for chunk in input:
        good_syntax = True
        to_resolve = []
        for c in chunk:
            if c in closing_brackets: 
                matching_character = opening_brackets[closing_brackets.index(c)]
            if c in opening_brackets: 
                to_resolve.append(c)
            else:
                if to_resolve.pop()  != matching_character:
                    good_syntax = False
                    break
        if good_syntax and to_resolve:
            total_score = 0
            to_resolve.reverse() 
            for c in to_resolve:
                total_score = total_score*5 + opening_brackets.index(c) + 1               
            error_scores.append(total_score)
    error_scores.sort()
    ans = error_scores[len(error_scores) // 2]
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 26397
    assert part2(test_input) == 288957

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 