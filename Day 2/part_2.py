def is_safe(levels):
    is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels) - 1))
    is_decreasing = all(levels[i+1] < levels[i] for i in range(len(levels) - 1))
    diffs = [levels[i+1] - levels[i] for i in range(len(levels) - 1)]
    if ((is_increasing or is_decreasing) and all(1 <= diff <= 3 for diff in diffs)):
        return True
    return False

def count_safe_reports(data):
    safe_count = 0

    for levels in data:
        # Check if the report is already safe
        if is_safe(levels):
            safe_count += 1
            continue
        # Check if removing one level can make the report safe
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]
            if is_safe(new_levels):
                safe_count += 1
                break  # No need to check further; we found a solution for this report

    return safe_count