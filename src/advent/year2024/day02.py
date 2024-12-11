def read_reports() -> list[list[int]]:
    reports = []
    with open("day02.txt", "r") as fp:
        for line in fp.readlines():
            report = [int(level) for level in line.split()]
            reports.append(report)

    return reports


def is_report_safe(report: list[int]):
    diffs = []
    for i in range(1, len(report)):
        diffs.append(report[i - 1] - report[i])
    return all(1 <= diff <= 3 for diff in diffs) or all(-1 >= diff >= -3 for diff in diffs)


reports = read_reports()
print(sum(is_report_safe(r) for r in reports))
print(sum([1 for r in reports if any([is_report_safe(r[:i] + r[i + 1:]) for i in range(len(r))])]))
