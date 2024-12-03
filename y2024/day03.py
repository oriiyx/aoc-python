import re

from util import reader


def part_1():
    memory_lines = reader.process_input("./y2024/day03.txt")
    memory_sum = 0
    for memory in memory_lines:
        # capturing 2 groups () ()
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, memory)
        for match in matches:
            memory_sum += (int(match[0]) * int(match[1]))
    print("part1: " + str(memory_sum))


def part_2():
    memory_lines = reader.process_input("./y2024/day03.txt")
    memory = ''
    for memory_part in memory_lines:
        memory += memory_part
    tokens = tokenize(memory)
    memory_sum = process_tokens(tokens)

    print("part2: " + str(memory_sum))


def tokenize(text):
    tokens = []
    # Find ALL instances of each pattern in the WHOLE text
    for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", text):
        x, y = map(int, match.groups())
        tokens.append((match.start(), "mul", (x, y)))

    for match in re.finditer(r"do\(\)", text):
        tokens.append((match.start(), "do", None))

    for match in re.finditer(r"don't\(\)", text):
        tokens.append((match.start(), "dont", None))

    # Sort all tokens by position
    return sorted(tokens)


def process_tokens(tokens):
    enabled = True
    result = 0

    for pos, cmd_type, data in tokens:
        if cmd_type == "mul" and enabled:
            x, y = data
            result += x * y
        elif cmd_type == "do":
            enabled = True
        elif cmd_type == "dont":
            enabled = False

    return result