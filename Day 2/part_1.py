def count_safe_reports(data):
    safe_count = 0

    for levels in data:
        is_increasing = all(levels[i+1] > levels[i] for i in range(len(levels) - 1))
        is_decreasing = all(levels[i+1] < levels[i] for i in range(len(levels) - 1))
        diffs = [abs(levels[i+1] - levels[i]) for i in range(len(levels) - 1)]
        if ((is_increasing or is_decreasing) and all(1 <= diff <= 3 for diff in diffs)):
            safe_count += 1
    
    return safe_count


