from advent import read_input

lines = read_input('day01.txt')


def starts_with_any(s, prefixes):
    for prefix in prefixes:
        if s.startswith(prefix):
            return prefix
    return False


codes = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
         'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
         }
s = 0
for l in lines:
    digits = []
    for i in range(len(l)):
        if l[i].isdigit():
            digits.append(l[i])
            continue
        digit_found = starts_with_any(l[i:], codes.keys())
        if digit_found:
            digits.append(codes[digit_found])

    s += int(digits[0] + digits[-1])

print(s)
