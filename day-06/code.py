def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split(",")
        input = list(map(int, input)) 
        return input

def count_fishes(fishes: list, days:int) -> int:
    fishes = [fishes.count(i) for i in range(9)]
    for _ in range(days):
        new_fishes = [0 for _ in range(9)]
        for i, _ in enumerate(fishes):
            if i == 0:
                new_fishes[6] = fishes[0]
                new_fishes[8] = fishes[0]
            else:
                new_fishes[i-1] += fishes[i]
        fishes = new_fishes.copy()
    return sum(fishes)

def part1(input: list, days: int) -> int:
    ans = count_fishes(input, days)
    return ans

def part2(input: list, days: int) -> int:
    ans = count_fishes(input, days)
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input, 18) == 26
    assert part2(test_input, 18) == 26

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input, 80))
    print(part2(input, 256)) 