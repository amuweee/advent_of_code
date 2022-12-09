# treetop tree house

with open("data/08.txt") as f:
    forest = f.readlines()

grid = [t.strip("\n") for t in forest]

trees = []
for i, x in enumerate(grid):
    for j, y in enumerate(x):
        trees.append((i, j, int(y)))

max_x = len(grid[0]) - 1
max_y = len(forest) - 1

visible = 0
for tree in trees:

    # print(f"--tree is {tree}")
    x = tree[0]
    y = tree[1]
    h = tree[2]

    if x > 0 and x < max_x and y > 0 and y < max_y:
        l = [t[2] for t in trees if t[0] == x and t[1] < y]
        r = [t[2] for t in trees if t[0] == x and t[1] > y]
        u = [t[2] for t in trees if t[1] == y and t[0] < x]
        d = [t[2] for t in trees if t[1] == y and t[0] > x]
        # print(f"  left: {l} right {r} up {u} down {d}")
        if h > max(l) or h > max(r) or h > max(u) or h > max(d):
            visible += 1
            # print(f"  visible, add to counter: {visible}")
        # else:
            # print("  not visible")
    else:
        visible += 1
        # print(f"  tree on edges add to counter: {visible}")

print(f"PART 1: total visible trees: {visible}")


def find_visibles(height, trees):
    counter = 0
    for t in trees:
        if height > t:
            counter += 1
        else:
            counter += 1
            return counter
    return counter

visible_score = []
for tree in trees:
    
    # print(f"--tree is {tree}")
    x = tree[0]
    y = tree[1]
    h = tree[2]

    if x > 0 and x < max_x and y > 0 and y < max_y:
        l = [t[2] for t in trees if t[0] == x and t[1] < y]
        r = [t[2] for t in trees if t[0] == x and t[1] > y]
        u = [t[2] for t in trees if t[1] == y and t[0] < x]
        d = [t[2] for t in trees if t[1] == y and t[0] > x]
        # print(f"  left: {l} right {r} up {u} down {d}")
        vis_l = find_visibles(h, reversed(l))
        vis_r = find_visibles(h, r)
        vis_u = find_visibles(h, reversed(u))
        vis_d = find_visibles(h, d)
        # print(f"  visibles are ({vis_l}, {vis_r}, {vis_u}, {vis_d})")
        visible_score.append((vis_l, vis_r, vis_u, vis_d))

scores = []
for vis in visible_score:
    view = 1
    for s in vis:
        if s > 0:
            view = view * s
    scores.append(view)

print(f"PART 2: max score is: {max(scores)}")

