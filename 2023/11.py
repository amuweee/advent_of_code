# monkey in the middle
from datetime import datetime as dt

with open("data/11.txt") as f:
    lines = f.readlines()
    lines = [l.strip("\n") for l in lines]
    lines = [l.lstrip().lower() for l in lines]

monkeys = []
monk = []
for l in lines:
    if l != "":
        monk.append(l)
    else:
        monkeys.append(monk)
        monk = []
monkeys.append(monk)


class Monkey:
    def __init__(self, lines) -> None:
        self.name: str = lines[0].strip(":")
        self.items: list[int] = [int(i.strip(",")) for i in lines[1].split()[2:]]
        self.op: list[str] = lines[2].split()[-2:]
        self.test: int = int(lines[3].split()[-1])
        self.tar_true: str = lines[4].strip("if true: throw to ")
        self.tar_false: str = lines[5].strip("if false: throw to ")
        self.inspected:int = 0
        self.next = None


class Troop:
    def __init__(self, monk: Monkey, worry: int) -> None:
        self.leader = monk
        self.worry_div = worry

    def add_follower(self, monk: Monkey):
        leader = self.leader
        leader.is_last = False
        monk.is_last = True
        while leader.next:
            leader = leader.next
            leader.is_last = False
        leader.next = monk

    def turn(self, monk: Monkey) -> list:
        items_thrown = []
        for item in monk.items:  # for all the items of monke
            item %= self.worry_div
            match monk.op:  # calculate new worry
                case ["+", "old"]:
                    worry = item + item
                case ["+", num]:
                    worry = item + int(num)
                case ["*", "old"]:
                    worry = item * item
                case ["*", num]:
                    worry = item * int(num)
            if worry % monk.test == 0:  # which monke to throw to
                target = monk.tar_true
            else:
                target = monk.tar_false
            items_thrown.append((target, worry))

        return items_thrown

    def do_round(self) -> None:
        monk = self.leader
        last_monk = False
        while not last_monk:
            items_thrown = self.turn(monk)  # get items thrown
            for i in items_thrown:  # append items
                recipient = self.leader
                while recipient.name != i[0]:
                    recipient = recipient.next
                recipient.items.append(i[1])
            monk.inspected += len(monk.items)  # track items and reset
            monk.items = []
            if not monk.is_last: # check if last for looping
                monk = monk.next
            else:
                last_monk = True


troop = Troop(Monkey(monkeys[0]), 3)
for m in monkeys[1:]:
    troop.add_follower(Monkey(m))

for i in range(20):
    troop.do_round()

last_monk = False
monk = troop.leader
business = []
while not last_monk:
    business.append(monk.inspected)
    if not monk.is_last:
        monk = monk.next
    else:
        last_monk = True
monkey_business = sorted(business)[-1] * sorted(business)[-2]
print(f"PART 1: level of monkey business is {monkey_business}")


# part deux
div = 5 * 11 * 2 * 13 * 7 * 3 * 17 * 19
troop = Troop(Monkey(monkeys[0]), div)
for m in monkeys[1:]:
    troop.add_follower(Monkey(m))

for i in range(10000):
    # print(f"round {i}")
    troop.do_round()

last_monk = False
monk = troop.leader
business = []
while not last_monk:
    business.append(monk.inspected)
    if not monk.is_last:
        monk = monk.next
    else:
        last_monk = True
monkey_business = sorted(business)[-1] * sorted(business)[-2]
print(f"PART 2: level of monkey business is {monkey_business}")

