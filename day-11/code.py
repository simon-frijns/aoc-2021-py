def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n")
        return input

def part1(input: list) -> int:
    ans = 0
    
    return ans

def part2(input: list) -> int:
    ans = 0

    return ans
    
def test():
    test_input = get_input("test_input.txt")
    print(part1(test_input))
    #assert part1(test_input) == 
    #assert part2(test_input) == 

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    #print(part1(input))
    #print(part2(input)) 