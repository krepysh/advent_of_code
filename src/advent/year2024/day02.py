def read_reports() -> list[list[int]]:
    reports = []
    with open("day02.txt", "r") as fp:
        for line in fp.readlines():
            report = [int(level) for level in line.split()]
            reports.append(report)

    return reports


def is_report_safe(report: list[int], tolerate_first_bad=False):
    prev = report[0]
    prev_diff = report[1] - prev
    for i in range(1, len(report)):
        current = report[i]
        diff = current - prev
        if abs(diff) > 3 or diff == 0:
            if tolerate_first_bad:
                tolerate_first_bad = False
                continue
            return False
        if diff // abs(diff) != prev_diff // abs(prev_diff):
            if tolerate_first_bad:
                tolerate_first_bad = False
                continue
            return False
        prev_diff = diff
        prev = current
    return True


if __name__ == "__main__":
    for r in read_reports():
        print(r)
        print(is_report_safe(r, tolerate_first_bad=True))
    # part 2
    print(sum([is_report_safe(r, tolerate_first_bad=True) for r in read_reports()]))