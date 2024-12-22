base = 16777216


def n_random(start, n):
    secret = start
    for i in range(n):
        secret = secret ^ (secret * 64)
        secret = secret % base
        secret = secret ^ (secret // 32)
        secret = secret % base
        secret = secret ^ (secret * 2048)
        secret = secret % base
    return secret


res = 0
for start in map(int, open(0).read().split()):
    res += (n_random(start, 2000))
print(res)
