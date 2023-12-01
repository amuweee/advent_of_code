# rucksack reorganization

with open("data/03.txt") as f:
    items_list = [l.strip("\n") for l in f.readlines()]

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = lower_case.upper()

priority = {}
for i, a in enumerate(lower_case + upper_case, 1):
    priority[a] = i


def sort_comps(items):

    list_items = [a for a in items]
    mid_point = len(list_items) / 2
    comp1 = []
    comp2 = []

    for i, a in enumerate(list_items):
        if i < mid_point:
            comp1.append(a)
        else:
            comp2.append(a)

    return comp1, comp2


# part 1
total_priority = 0
for items in items_list:
    comp1, comp2 = sort_comps(items)
    shared = [a for a in comp1 if a in comp2]
    total_priority += priority[shared[0]]
print(f"total priority on sorting is {total_priority}")

# part 2
alt_total_priority = 0
badges_list = []
elf = []
for i, items in enumerate(items_list, 1):
    if len(elf) < 3 and i != len(items_list):
        elf.append(items)
    elif i == len(items_list):
        elf.append(items)
        badges_list.append(elf)
    else:
        badges_list.append(elf)
        elf = []
        elf.append(items)

print(badges_list[-1])

for items in badges_list:
    rs1 = [a for a in items[0]]
    rs2 = [a for a in items[1]]
    rs3 = [a for a in items[2]]
    common = [a for a in rs1 if a in rs2 and a in rs3]
    alt_total_priority += priority[common[0]] 

print(f"alterbate priority on sorting is {alt_total_priority}")

