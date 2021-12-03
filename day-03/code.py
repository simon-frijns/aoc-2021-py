def get_input(filename: str) -> list:
    with open(filename) as input:
        input_list = input.read().strip().split("\n")
        return input_list

def part1(report:list) -> int:
    ans = 0
    gamma = epsilon = ""
    pivoted_report = [list(i) for i in zip(*report)] 
    for row in pivoted_report:
        if row.count('0') > row.count('1'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    ans = int(gamma, 2) * int(epsilon, 2)
    return ans

def find_rating(report: list, gas: str, column: int = 0) -> int:
    if len(report) == 1:
        return int(report[0], 2)
    pivoted_report = [list(i) for i in zip(*report)]
    row = pivoted_report[column]
    match gas:
        case 'co2': 
            digit = '0' if row.count('1') >= row.count('0') else '1'
        case 'oxygen':
            digit = '1' if row.count('1') >= row.count('0') else '0'
    report = [row for row in report if row[column] == digit]
    column += 1
    return find_rating(report, gas, column)

def part2(report: list) -> int:
    ans = 0
    oxygen = find_rating(report, 'oxygen')
    co2 = find_rating(report, 'co2')
    ans = oxygen * co2
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 198
    assert part2(test_input) == 230

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 