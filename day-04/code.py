from typing import Tuple
import re

def get_input(filename: str) -> list:
    with open(filename) as input:
        input = input.read().strip().split("\n\n")
        return input

def parse_input(input: list) -> Tuple[list, list]:
    numbers = input[0].split(',')
    numbers = list(map(int, numbers)) 
    boards = []
    for line in input[1:]:
        board = []
        board_rows = line.split('\n')
        for board_row in board_rows:
            board_nums = list(map(int, re.findall('\d+', board_row)))
            board.append(board_nums)
        boards.append(board)
    return numbers, boards

def play_round(number: int, boards:list, board_status: list) -> list:
    for board in range(len(boards)):
            for row in range(len(boards[0])):
                for col in range(len(boards[0][0])):
                    if boards[board][row][col] == number:
                        board_status[board][row][col] = 1
    return board_status
    
def check_winner(board_status: list) -> bool:  
    winning_board = False
    sum_rows = [sum(row) for row in board_status]
    sum_cols = [sum(col) for col in zip(*board_status)]
    if 5 in sum_rows + sum_cols: # not a fan but it works
        winning_board = True
    return winning_board

def compute_result(number: int, board:list, board_status: list) -> int:
    result = 0
    for row in range(len(board[0])):
        for col in range(len(board[0])):
            if board_status[row][col] == 0:
                result += board[row][col]
    result *= number
    return result

def play_bingo(input:list) -> dict:
    numbers, boards = parse_input(input)
    board_status = []
    winning_boards = {}
    for _ in boards:
        board_status.append([[0 for _ in range(len(boards[0][0]))] for _ in range(len(boards[0]))])  # Creates a 5x5 of 0s
    for number in numbers:
        board_status = play_round(number, boards, board_status)
        for i, _ in enumerate(board_status):
            if i in winning_boards: # only compute result when the win happens
                continue
            winning_board = check_winner(board_status[i])
            if winning_board:  
                winning_boards[i] = compute_result(number, boards[i], board_status[i])
    return winning_boards

def part1(input:list) -> int:
    ans = 0
    winning_boards = play_bingo(input)
    ans = list(winning_boards.values())[0]
    return ans

def part2(input: list) -> int:
    ans = 0
    winning_boards = play_bingo(input)
    ans = list(winning_boards.values())[-1]
    return ans
    
def test():
    test_input = get_input("test_input.txt")
    assert part1(test_input) == 4512
    assert part2(test_input) == 1924

if __name__ == "__main__":
    test()
    input = get_input("input.txt")
    print(part1(input))
    print(part2(input)) 