# Calorie counting

with open("data/01.txt") as f:
    data = f.readlines()

ints = [int(d.strip('\n')) if d != '\n' else 0 for d in data]

elves = []
temp = 0
for i in ints:
    if i != 0:
        temp += i
    else:
        elves.append(temp)
        temp = 0

# part 1
print(f"the top elf carries: {max(elves)}")

# part 2
elves.sort(reverse=True)
top3 = 0
for i, c in enumerate(elves, 1):
    if i < 4:
        top3 += c
print(f"the top 3 elves carries: {top3}")
