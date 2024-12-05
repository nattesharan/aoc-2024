def is_valid_update(update, rules):
    for x, y in rules:
        if x in update and y in update:
            # x should appear before y if it  violtaes this in update then its invalid update
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    mid_index = len(update) // 2
    return update[mid_index]

def topological_sort(update, rules):
    from collections import defaultdict, deque

    # Build graph and in-degree count
    adj_list = defaultdict(list)
    in_degree = defaultdict(int)
    # create an adj list thinking rules as edges
    for x, y in rules:
        if x in update and y in update:
            adj_list[x].append(y)
            in_degree[y] += 1
    queue = deque()
    # Find all nodes with no incoming edges
    for node in update:
        if in_degree[node] == 0:
            queue.append(node)
    
    sorted_pages = []

    while queue:
        node = queue.popleft()
        sorted_pages.append(node)

        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def process_updates(rules, updates):
    invalid_updates = []

    for update in updates:
        if not is_valid_update(update, rules):
            invalid_updates.append(update)

    # fix invalid updates
    corrected_updates = [topological_sort(update, rules) for update in invalid_updates]

    corrected_middle_pages = [find_middle_page(update) for update in corrected_updates]

    return sum(corrected_middle_pages)


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        sections = text.strip().split("\n\n")
        rules_str, updates_str = sections
        rules = [tuple(map(int, rule.split('|'))) for rule in rules_str.splitlines()]
        updates = [list(map(int, update.split(','))) for update in updates_str.splitlines()]
        print(process_updates(rules, updates))