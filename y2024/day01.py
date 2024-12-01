import bisect

from util import reader


def part_1():
    lines = reader.process_input("./y2024/day01.txt")
    left_list = []
    right_list = []
    sum_diff = 0
    for line in lines:
        split = line.split("   ")
        bisect.insort(left_list, split[0])
        bisect.insort(right_list, split[1])

    for i in range(len(lines)):
        sum_diff += abs(int(left_list[i]) - int(right_list[i]))

    print(sum_diff)


def part_2():
    lines = reader.process_input("./y2024/day01.txt")
    left_list = []
    right_list = {}
    similarity_score = 0
    for line in lines:
        split = line.split("   ")
        left_list.append(split[0])
        right_list[split[1]] = right_list.get(split[1], 0) + 1

    for num in left_list:
        similarity_score += right_list.get(num, 0) * int(num)

    print(similarity_score)