# supply stacks

with open("data/05.txt") as f:
    lines = f.read().split("\n")

initial = lines[:8]
stacks = {k: [] for k in range(1, 10)}

for row in initial:
    row_chars = [a for a in row]
    char_w_pos = zip([i for i in range(len(row_chars))], row_chars)
    for c in char_w_pos:
        if not c[1] in (" ", "[", "]"):
            if c[0] == 1:
                stacks[1].append(c[1])
            elif c[0] == 5:
                stacks[2].append(c[1])
            elif c[0] == 9:
                stacks[3].append(c[1])
            elif c[0] == 13:
                stacks[4].append(c[1])
            elif c[0] == 17:
                stacks[5].append(c[1])
            elif c[0] == 21:
                stacks[6].append(c[1])
            elif c[0] == 25:
                stacks[7].append(c[1])
            elif c[0] == 29:
                stacks[8].append(c[1])
            elif c[0] == 33:
                stacks[9].append(c[1])


move_set = [(a.split()[1], a.split()[3], a.split()[5]) for a in lines[10:-1]]

# part 1
def move_one_at_time(move_set, stacks):

    for k, v in stacks.items():
        stacks[k] = [a for a in reversed(v)]

    for move in move_set:
        supplies = int(move[0])
        origin = int(move[1])
        dest = int(move[2])

        for i in range(supplies):
            stacks[dest].append(stacks[origin].pop())

    top_crates = "".join([v[-1] for v in stacks.values()])
    print(top_crates)

# move_one_at_time(move_set, stacks)

# part 2
def move_multi_at_time(move_set, stacks):
    
    for move in move_set:
        supplies = int(move[0])
        origin = int(move[1])
        dest = int(move[2])

        crates = stacks[origin][:supplies]
        stacks[dest] = crates + stacks[dest]
        stacks[origin] = stacks[origin][supplies:]

    top_crates = "".join([v[0] for v in stacks.values()])
    print(top_crates)

move_multi_at_time(move_set, stacks)
    


