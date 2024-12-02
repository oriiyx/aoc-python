from util import reader


def part_1_2():
    reports = reader.process_input("./y2024/day02.txt")
    safe_reports = 0
    unsafe_reports = []
    for report in reports:
        levels = [int(x) for x in report.split(" ")]
        if is_sorted(levels):
            is_safe = check_differ(levels)
        else:
            is_safe = False
        if is_safe:
            safe_reports += 1
        else:
            unsafe_reports.append(levels)

    print(safe_reports)

    for levels in unsafe_reports:
        i = 0
        damped = False
        while not damped:
            test_levels = levels.copy()
            test_levels.pop(i)
            if is_sorted(test_levels) and check_differ(test_levels):
                safe_reports += 1
                break
            i += 1
            if i == len(levels):
                damped = True

    print(safe_reports)


def is_sorted(l):
    # strictly increasing
    if all(l[i] < l[i + 1] for i in range(len(l) - 1)):
        return True
    # strictly decreasing
    return all(l[i] > l[i + 1] for i in range(len(l) - 1))


def check_differ(levels):
    previous_level = levels[0]
    for level in levels[1:]:
        diff = abs(level - previous_level)
        if diff < 1 or diff > 3:  # minimum and maximum diff
            return False
        previous_level = level
    return True
