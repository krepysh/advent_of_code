from advent import read_input


lines = read_input('day08.txt')
trees = []
for l in lines:
    trees.append([])
    for tree in l:
        trees[-1].append(int(tree))



H = len(lines)
W = len(lines[0])

def is_visible(height, width):
    val = trees[height][width]
    highest_left = all([t < val for t in trees[height][0:width]])
    highest_right = all([t < val for t in trees[height][width+1:]])
    col = [trees[i][width] for i in range(len(trees))]
    highest_top = all([t < val for t in col[0:height]])
    highest_bottom = all([t < val for t in col[height+1:]])
    return any([highest_bottom, highest_top, highest_right, highest_left])

r = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        r += is_visible(i, j)

print(r)

scores = []


def vd_horizontal(i, j):
    vd_left = 0
    vd_right = 0
    row = trees[i]
    val = row[j]
    for k in range(j+1, len(row)):
        vd_right += 1
        if row[k] >= val:
            break

    for k in range(j-1, -1, -1):
        vd_left += 1
        if row[k] >= val:
            break
    return vd_left * vd_right


def vd_vertical(i, j):
    vd_top, vd_bottom = 0, 0
    col = [trees[k][j] for k in range(len(trees))]
    val = col[i]
    for k in range(i+1, len(col)):
        vd_top += 1
        if col[k] >= val:
            break

    for k in range(i-1, -1, -1):
        vd_bottom += 1
        if col[k] >= val:
            break
    return vd_top * vd_bottom


for i in range(1, len(trees)-1):
    for j in range(1, len(trees[0])-1):
        score = vd_horizontal(i, j) * vd_vertical(i, j)
        scores.append(score)

print(max(scores))
