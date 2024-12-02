from util import reader


def part_1():
    reports = reader.process_input("./y2024/day02.txt")
    safe_reports = 0
    for report in reports:
        levels = [int(x) for x in report.split(" ")]
        is_safe = True
        if is_sorted(levels):
            previous_level = levels[0]
            for level in levels[1:]:
                diff = abs(level - previous_level)
                if diff < 1 or diff > 3:  # Check both minimum and maximum difference
                    is_safe = False
                    break
                previous_level = level
        else:
            is_safe = False
        if is_safe:
            safe_reports += 1
    print(safe_reports)


def part_2():
    reports = reader.process_input("./y2024/day02.txt")
    safe_reports = 0
    for report in reports:
        levels = [int(x) for x in report.split(" ")]
        is_safe = True
        problem_dampener_used = False
        if is_sorted(levels):
            previous_level = levels[0]
            for level in levels[1:]:
                diff = abs(level - previous_level)
                previous_level = level
                if diff < 1 or diff > 3:  # Check both minimum and maximum difference
                    if not problem_dampener_used:
                        problem_dampener_used = True
                        continue
                    is_safe = False
                    break
        else:
            is_safe = False
        if is_safe:
            safe_reports += 1
    print(safe_reports)

def is_sorted(l):
    # Check strictly increasing
    if all(l[i] < l[i + 1] for i in range(len(l) - 1)):
        return True
    # Check strictly decreasing
    return all(l[i] > l[i + 1] for i in range(len(l) - 1))
