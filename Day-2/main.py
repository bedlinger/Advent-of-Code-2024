def part_one(data):
    print("Part 1")
    safe_reports: int = 0

    for report in data:
        if is_report_safe(report):
            safe_reports += 1

    print(f"\tSafe Reports: {safe_reports}")

def part_two(data):
    print("Part 2")
    safe_reports: int = 0

    for report in data:
        if is_report_safe(report):
            safe_reports += 1
        else:
            found_safe = False
            for i in range(len(report)):
                new_report = report[:i] + report[i+1:]
                if is_report_safe(new_report):
                    found_safe = True
                    break
            if found_safe:
                safe_reports += 1

    print(f"\tSafe Reports: {safe_reports}")

def is_report_safe(report) -> bool:
    is_increasing = all(int(report[i]) < int(report[i + 1]) for i in range(len(report) - 1))
    is_decreasing = all(int(report[i]) > int(report[i + 1]) for i in range(len(report) - 1))

    if not (is_increasing or is_decreasing):
        return False
    else:
        for i in range(len(report) - 1):
            dist = abs(int(report[i]) - int(report[i + 1]))
            if dist < 1 or dist > 3:
                return False
    return True

def main():
    data = []
    with open("./input.txt", "r") as f:
        for report in f:
            data.append(report.split())

    part_one(data)
    part_two(data)

if __name__ == "__main__":
    main()
