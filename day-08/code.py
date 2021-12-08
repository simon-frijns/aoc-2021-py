from typing import Tuple

digits = [
     'abcefg'
    ,'cf'
    ,'acdeg'
    ,'acdfg'
    ,'bcdf'
    ,'abdfg'
    ,'abdefg'   
    ,'acf'  
    ,'abcdefg'       
    ,'abcdfg'
]

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        return input

def parse_input(line: str) -> Tuple[list, list]:
    p, o = line.split(' | ')
    patterns = [sorted(pattern) for pattern in p.split(' ')]
    outputs = [sorted(output) for output in o.split(' ')]
    return patterns, outputs

def part1(input: list) -> int:
    ans = 0
    for line in input:
        _, outputs = parse_input(line)
        to_find = [len(digits[i]) for i in (1, 4, 7, 8)]
        ans += sum([len(word) in to_find for word in outputs])
    return ans

def part2(input: list) -> int:
    ans = 0
    for line in input:
        segment_mapping = {}
        patterns, outputs = parse_input(line) 

        for i in (1, 4, 7, 8):
            segment_mapping[i] = [p for p in patterns if len(p) == len(digits[i])][0]

        snz_subset = [p for p in patterns if len(p) == len(digits[6])]
        for i in snz_subset: 
            if all(c in i for c in segment_mapping[4]):
                segment_mapping[9] = i
                snz_subset.remove(i)
        for i in snz_subset: 
            if all(c in i for c in segment_mapping[1]):
                segment_mapping[0] = i
                snz_subset.remove(i)
        segment_mapping[6] = snz_subset[0] 

        ttf_subset = [p for p in patterns if len(p) == len(digits[2])]
        for i in ttf_subset: 
            if all(c in i for c in segment_mapping[1]):
                segment_mapping[3] = i
                ttf_subset.remove(i)
        for i in ttf_subset: 
            if len([c for c in i if c in segment_mapping[4]]) == 3:
                segment_mapping[5] = i
                ttf_subset.remove(i)
        segment_mapping[2] = ttf_subset[0]     

        a = ''
        for i in outputs:
            for number, value in segment_mapping.items():
                if i == value:
                    a += str(number)
        ans += int(a)
    return ans

def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 26
    assert part2(test_input) == 61229

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 