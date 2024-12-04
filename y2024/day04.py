from util import reader


def part_1():
    lines = reader.process_input("./y2024/day04.txt")
    count = find_xmas(lines)
    print(count)


def find_xmas(grid):
    rows = len(grid)
    columns = len(grid[0])
    count = 0

    directions = [
        (0, 1),  # right
        (1, 1),  # down-right
        (1, 0),  # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1),  # up-left
        (-1, 0),  # up
        (-1, 1)  # up-right
    ]

    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < columns

    def check_xmas(row, col, direction):
        dx, dy = direction
        chars = []
        for i in range(4):
            check_row = row + (dx * i)
            check_col = col + (dy * i)
            if not is_valid_position(check_row, check_col):
                return False
            chars.append(grid[check_row][check_col])
        return ''.join(chars) == 'XMAS'

    for i in range(rows):
        for j in range(columns):
            for direction in directions:
                if check_xmas(i, j, direction):
                    count += 1

    return count


def part_2():
    lines = reader.process_input("./y2024/day04.txt")
    count = find_mas(lines)
    print(count)


def find_mas(grid):
    rows = len(grid)
    columns = len(grid[0])
    count = 0

    def is_not_valid(x, y):
        valid = 0 <= x < rows and 0 <= y < columns
        return valid is not True

    def middle_out(row, col):
        if is_not_valid(row-1, col-1) or is_not_valid(row+1, col+1) or is_not_valid(row-1, col+1) or is_not_valid(row+1, col-1):
            return False

        top_left_to_bottom_right = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
        top_right_to_bottom_left = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]

        valid_strings = {"MAS", "SAM"}
        if top_left_to_bottom_right in valid_strings and top_right_to_bottom_left in valid_strings:
            return True

    for i in range(rows):
        for j in range(columns):
            if middle_out(i, j):
                count += 1

    return count
