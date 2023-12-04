from advent import read_input


def not_empty(x):
    return x


cards = read_input('day04.txt')
copies_won = [0] * len(cards)

res = 0
for card_num, raw_line in enumerate(cards):
    card, numbers = raw_line.split(': ')
    winning_number, current_numbers = numbers.split(' | ')
    winning_number = list(filter(not_empty, winning_number.strip().split(' ')))
    current_numbers = list(filter(not_empty, current_numbers.strip().split(' ')))
    lucky_numbers = 0
    for num in current_numbers:
        if num in winning_number:
            lucky_numbers += 1
    instances_of_current_card = 1 + copies_won[card_num]
    for i in range(lucky_numbers):
        copies_won[card_num + 1 + i] += instances_of_current_card
    point_pow = lucky_numbers - 1
    res += (2 ** point_pow) if point_pow >= 0 else 0

print(res)
total_cards = sum(copies_won) + len(cards)
print(f'part 2:{total_cards}')
