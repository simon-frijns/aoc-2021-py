def get_input(filename: str) -> list:
    with open(filename) as input:
        input_list = input.read().strip().split("\n")
        input_list = list(map(int, input_list)) 
        return input_list

def part1(measurements:list) -> int:
    ans = 0
    measurements_to_compare = [*zip(measurements, measurements[1:])]
    ans = [x < y for x, y in measurements_to_compare].count(True) 
    return ans

def part2(measurements: list) -> int:
    ans = 0
    window = 3
    sums = []
    for i in range(len(measurements) - window + 1): # rolling window
        sums.append(sum(measurements[i:i + window]))
    ans = part1(sums) # re-use p1
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 7
    assert part2(test_input) == 5

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 