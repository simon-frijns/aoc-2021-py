def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split(",")
        input = list(map(int, input)) 
        return input

def cost(distance):
        return distance * (distance+1) // 2

def part1(input: list) -> int:
    possible_answers = set(input)
    ans_list = []
    for answer in possible_answers:
        ans_list.append(sum([abs(pos - answer) for pos in input]))
    return min(ans_list)

def part2(input: list) -> int:
    possible_answers = range(max(input))
    ans_list = []
    for answer in possible_answers:
        ans_list.append(sum([cost(abs(pos - answer)) for pos in input]))
    return min(ans_list)
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 37
    assert part2(test_input) == 168

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 