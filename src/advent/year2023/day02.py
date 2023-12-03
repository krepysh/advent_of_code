from advent import read_input


lines = read_input('day02.txt')

rgb = (12, 13, 14)
colors = ['red', 'green', 'blue']

impossible_games = []
possible_games = []
min_sets = []
for game in lines:
    game_num, rounds = game.split(': ')
    game_num = game_num.split(' ')[1]
    game_possible = True
    min_set = [0, 0, 0]
    for single_round in rounds.split('; '):
        for cubes in single_round.split(', '):
            # print(cubes )
            count, color = cubes.split(' ')
            count = int(count)
            index = colors.index(color)
            min_set[index] = max(count, min_set[index])
            if count > rgb[index] and game_num not in impossible_games:
                impossible_games.append(game_num)
                game_possible = False
    min_sets.append(min_set)
    if game_possible:
        possible_games.append(game_num)

pows = [ms[0] * ms[1] * ms[2] for ms in min_sets]
part2 = sum(pows)

print(sum(map(int, possible_games)))
print(part2)

