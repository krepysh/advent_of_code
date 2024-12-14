rules_part, updates_part = open(0).read().split('\n\n')
rules = [tuple(map(int, rule.split("|"))) for rule in rules_part.splitlines()]
updates = [list(map(int, update.split(","))) for update in updates_part.splitlines()]

part1_res = 0
part2_res = 0


def is_update_safe(update: list[int], try_to_fix=False):
    local_rules = []
    for page in update:
        for rule in rules:
            if page in rule:
                local_rules.append(rule)
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            for rule in local_rules:
                if (update[j], update[i]) == rule:
                    if try_to_fix:
                        update[i], update[j] = update[j], update[i]
                        continue
                    return False
    return True


for update in updates:
    if is_update_safe(update):
        part1_res += update[len(update) // 2]
    else:
        while not is_update_safe(update, try_to_fix=True):
            ...
        part2_res += update[len(update) // 2]

print(part1_res)
print(part2_res)