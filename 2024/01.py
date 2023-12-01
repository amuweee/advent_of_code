# Trebuchet?!

with open("data/01.txt") as f:
    data = f.readlines()


def get_calibration_val(line):
    vals = [v for v in line if v.isdigit()]
    return vals[0] + vals[-1]


total = 0
for line in data:
    cal = get_calibration_val(line)
    total += int(cal)

print(total)

# part 2
alpha_num = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

valid_alphas = list(alpha_num.keys())


def find_all_valids(line):
    valids = []
    for index, char in enumerate(line):
        if char.isdigit():
            valids.append(char)
        else:
            counter = 1
            while (
                line[index : index + counter] not in valid_alphas
                    and len(line[counter:]) > 0
            ):
                counter += 1
            if line[index : index + counter] in valid_alphas:
                valids.append(alpha_num[line[index : index + counter]])
    return valids[0] + valids[-1]


total = 0
for line in data:
    cal = find_all_valids(line)
    total += int(cal)
print(total)
