# tuning trouble

with open("data/06.txt") as f:
    signal = f.read()

def first_signal(signal, distinct):
    check = []
    for i, c in enumerate(signal, 1):
        if i <= distinct:
            check.append(c)
        else:
            check.append(c)
            subset = check[-distinct:]
            if len(set(subset)) == distinct:
                return i

print(first_signal(signal, 4))
print(first_signal(signal, 14))
