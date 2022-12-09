# camp cleanup

with open("data/04.txt") as f:
    pairs = f.read().split('\n')[:-1]

def get_sections(pair):
    
    s1 = pair.split(",")[0]
    s2 = pair.split(",")[1]
    s1low = int(s1.split('-')[0])
    s1up = int(s1.split('-')[1])
    s2low = int(s2.split('-')[0])
    s2up = int(s2.split('-')[1])

    return s1low, s1up, s2low, s2up

# part 1
overlaps = 0
for p in pairs:
    s1low, s1up, s2low, s2up = get_sections(p)
    if s1low <= s2low and s1up >= s2up:
        overlaps += 1
    elif s2low <= s1low and s2up >= s1up:
        overlaps += 1
    else:
        continue
print(f"pairs that have a full overlaps: {overlaps}")

# part 2
partial_overlap = 0
for p in pairs:
    s1low, s1up, s2low, s2up = get_sections(p)
    r1 = [i for i in range(s1low, s1up + 1)]
    r2 = [i for i in range(s2low, s2up + 1)]
    if len(set(r1 + r2)) != len(r1 + r2):
        partial_overlap += 1

print(f"pairs that have a partial overlaps: {partial_overlap}")
