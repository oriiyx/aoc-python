from util import reader
from collections import defaultdict, deque
from typing import List, Set, Dict, Tuple, Any


def parse_rules(rules_lines: List[str]) -> List[Tuple[int, int]]:
    rules = []
    for line in rules_lines:
        if not line.strip():  # Skip empty lines
            continue
        before, after = map(int, line.split('|'))
        rules.append((before, after))
    return rules


def parse_updates(updates_lines: List[str]) -> List[List[int]]:
    updates = []
    for line in updates_lines:
        if not line.strip():  # Skip empty lines
            continue
        update = list(map(int, line.split(',')))
        updates.append(update)
    return updates


def is_valid_update(update: List[int], rules: List[Tuple[int, int]]):
    """Check if an update satisfies all applicable rules"""
    update_set = set(update)

    # Only consider rules where both numbers are in the update
    applicable_rules = [rule for rule in rules
                        if rule[0] in update_set and rule[1] in update_set]

    # For each applicable rule, check if the "before" page comes before the "after" page
    for before, after in applicable_rules:
        before_idx = update.index(before)
        after_idx = update.index(after)
        if before_idx > after_idx:  # Rule violation
            return False

    return True


def get_middle_number(update: List[int]):
    return update[len(update) // 2]


def part_1():
    rules_lines = reader.process_input("./y2024/day05_1.txt")
    updates_lines = reader.process_input("./y2024/day05_2.txt")

    rules = parse_rules(rules_lines)
    updates = parse_updates(updates_lines)

    valid_updates = []
    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)

    result = sum(get_middle_number(update) for update in valid_updates)

    print(f"Part 1: {result}")


def build_graph(rules: List[Tuple[int, int]], pages: Set[int]):
    """
    Build adjacency list graph from rules, only including pages that are in the update.
    Returns a dict mapping page number to set of pages that must come after it.
    """
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    # Only include rules where both pages are in our update
    for before, after in rules:
        if before in pages and after in pages:
            graph[before].add(after)
            in_degree[after] += 1
            # Ensure both nodes are in the graph even if they have no outgoing edges
            if before not in in_degree:
                in_degree[before] = 0

    return graph, in_degree


def topological_sort(graph: Dict[int, Set[int]], in_degree: Dict[int, int]):
    """
    Perform topological sort using Kahn's algorithm.
    Returns sorted list of page numbers.
    """
    result = []
    queue = deque([page for page, deg in in_degree.items() if deg == 0])

    while queue:
        current = queue.popleft()
        result.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


def part_2():
    rules_lines = reader.process_input("./y2024/day05_1.txt")
    updates_lines = reader.process_input("./y2024/day05_2.txt")

    rules = parse_rules(rules_lines)
    updates = parse_updates(updates_lines)

    result = 0
    for update in updates:
        if not is_valid_update(update, rules):
            graph, in_degree = build_graph(rules, set(update))

            # Get correct order using topological sort
            correct_order = topological_sort(graph, in_degree)

            # Get middle number and add to sum
            middle_index = len(correct_order) // 2
            result += correct_order[middle_index]

    print(f"Part 2: {result}")

