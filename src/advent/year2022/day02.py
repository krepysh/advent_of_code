def read_input():
    filename = 'day02.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines


moves = read_input()


choices = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
order = ['rock', 'scissors', 'paper']


class Choice:
    scores = {'rock': 1, 'scissors': 3, 'paper': 2}

    def __init__(self, letter_choice):
        self.figure = choices[letter_choice]

    def __gt__(self, other):
        my_index = order.index(self.figure)
        shift = 1 - my_index
        other_index = (order.index(other.figure) + shift) % 3
        return other_index == 2

    def __eq__(self, other):
        return self.figure == other.figure

    def base_score(self):
        return self.scores[self.figure]

    def get_higher(self):
        my_index = order.index(self.figure)
        shift = 1 - my_index
        other_index = 0 - shift
        rv = Choice('A')
        rv.figure = order[other_index]
        return rv

    def get_lower(self):
        my_index = order.index(self.figure)
        shift = 1 - my_index
        other_index = 2 - shift
        rv = Choice('A')
        rv.figure = order[other_index % 3]
        return rv



def parse_move(move):
    their_str, ours_str = move.split()
    return Choice(their_str), Choice(ours_str)


score_1 = 0
score_2 = 0
DRAW = 'Y'
WIN = 'Z'
LOOSE = 'X'

for move in moves:
    their, ours = parse_move(move)
    planned_result = move.split()[1]
    if planned_result == DRAW:
        planned_move = their
        score_2 += their.base_score() + 3
    elif planned_result == LOOSE:
        planned_move = their.get_lower()
        score_2 += planned_move.base_score()
    elif planned_result == WIN:
        planned_move = their.get_higher()
        score_2 += planned_move.base_score() + 6
    print(their.figure, planned_move.figure, planned_result)
    if ours == their:
        score_1 += 3
    elif ours > their:
        score_1 += 6
    score_1 += ours.base_score()

print(score_1)
print(score_2)

