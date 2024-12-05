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

def process_updates(rules, updates):
    valid_updates = []
    
    for update in updates:
        if is_valid_update(update, rules):
            valid_updates.append(update)
    
    middle_pages = [find_middle_page(update) for update in valid_updates]
    return sum(middle_pages)

if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()
        sections = text.strip().split("\n\n")
        rules_str, updates_str = sections
        rules = [tuple(map(int, rule.split('|'))) for rule in rules_str.splitlines()]
        updates = [list(map(int, update.split(','))) for update in updates_str.splitlines()]
        print(process_updates(rules, updates))