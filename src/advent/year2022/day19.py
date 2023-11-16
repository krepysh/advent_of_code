from advent import read_input

GEODES = 0

OBSIDIAN = 1

CLAY = 2

ORE = 3

lines = read_input('day19.txt')

raw_blueprint = lines[0]
given_time = 24


def parse_price(price):
    rv = []
    for price in price.split(' and '):
        num, resource_name = price.split(' ')
        num = int(num)
        rv.append((num, resource_name.strip('.')))
    return rv


def parse_blueprint(raw_blueprint):
    id_part, quantities_part = raw_blueprint.split(': ')
    id_num = int(id_part.split(' ')[1])
    ore, clay, obsidian, geode = quantities_part.split('. ')
    ore_price = ore.split('costs ')[1]
    clay_price = clay.split('costs ')[1]
    obsidian_price = obsidian.split('costs ')[1]
    geode_price = geode.split('costs ')[1]
    return id_num, parse_price(ore_price), parse_price(clay_price), parse_price(obsidian_price), parse_price(geode_price)


def has_enough(resources, robot_price):
    for r_num, r_name in robot_price:
        if resources[r_name] < r_num:
            return False
    return True


def decrement_resources(resources, robot_price):
    for r_num, r_name in robot_price:
        resources[r_name] -= r_num


blueprint = parse_blueprint(raw_blueprint)

ore_robot_price = blueprint[1]

price = 2
ore = 0
ore_robots = 1
memo = {}
prices = blueprint[1::][::-1]
name_to_ind = {'ore': ORE, }

res_names = ('geodes', 'obsidian', 'clay', 'ore')


def dfs(resources, robots, steps_remain):
    if steps_remain == 0:
        return resources[OBSIDIAN]
    key = (resources, robots, steps_remain)
    if key in memo:
        return memo[key]
    steps = ['wait']
    results = []
    maxval = resources[OBSIDIAN] + robots[OBSIDIAN] * steps_remain
    for robot_type in (ORE, CLAY, OBSIDIAN):
        for val, res_name in prices[robot_type]:
            if resources[res_names.index(res_name)] < val:
                continue
            steps.append(res_names[robot_type])
    for s in steps:
        geodes, obsidian, clay, ore = resources
        geodes_robots, obsidian_robots, clay_robots, ore_robots = robots
        if s == 'ore':
            ore -= price
            ore_robots += 1
        elif s == 'clay':
            ore -= prices[CLAY][0][0]
            clay_robots += 1
        elif s == 'obsidian':
            ore -= prices[OBSIDIAN][0][0]
            clay -= prices[OBSIDIAN][1][0]
            obsidian_robots += 1
        ore += robots[ORE]
        clay += robots[CLAY]
        obsidian += robots[OBSIDIAN]
        geodes += robots[GEODES]
        resources_new = (geodes, obsidian, clay, ore)
        robots_new = (geodes_robots, obsidian_robots, clay_robots, ore_robots)
        results.append(dfs(resources_new, robots_new, steps_remain - 1))
    rv = max(results)
    memo[key] = rv
    return rv


res = (0, 0, 0, 0)
robots = (0, 0, 0, 1)
print(dfs(res, robots, 24))
print(blueprint)
