# rope bridge
from pprint import pprint

with open("data/09.txt") as f:
    moveset = f.readlines()
moveset = [m.strip("\n").split() for m in moveset]
moveset = [(m[0], int(m[1])) for m in moveset]
# print(f"total moveset: {moveset}")

H = [0, 0]
T = [0, 0]

movement = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def move_rope(H, T, move):

    H = [H[x] + move[x] for x in range(2)]  # move head
    x_diff = H[0] - T[0]
    y_diff = H[1] - T[1]

    if x_diff == 2:
        return H, [H[0] - 1, H[1]]
    elif x_diff == -2:
        return H, [H[0] + 1, H[1]]
    elif y_diff == 2:
        return H, [H[0], H[1] - 1]
    elif y_diff == -2:
        return H, [H[0], H[1] + 1]
    else:  # still touching
        return H, T


tail_pos = []
for move in moveset:
    for i in range(move[1]):
        H, T = move_rope(H, T, movement[move[0]])
        # print(f"head {H} tail {T}")
        tail_pos.append(T)

unique_pos = []
for p in tail_pos:
    if p not in unique_pos:
        unique_pos.append(p)

print(f"PART 1: num of unique tail position is {len(unique_pos)}")

# part deux
class Knot:
    def __init__(self, name, pos=[0, 0]) -> None:
        self.name = name
        self.pos = pos
        self.next = None


class Rope:
    def __init__(self, head=None) -> None:
        self.head = head

    def get_tail(self):
        head = self.head
        while head.next:
            head = head.next
        return head

    def get_all_pos(self):
        head = self.head
        coords = []
        while head.next:
            coords.append(head.pos)
            head = head.next
        coords.append(head.pos)
        return coords

    def append(self, node) -> None:
        head = self.head
        if head:
            while head.next:
                head = head.next
            head.next = node
        else:
            self.head = node

    def check_moves(self, H, T):
        # H = [H[x] + move[x] for x in range(2)]  # move head
        x_diff = H[0] - T[0]
        y_diff = H[1] - T[1]

        if abs(x_diff) + abs(y_diff) == 4: # diagonal movement!!!!
            return H, [int(H[0] - (x_diff / 2)), int(H[1] - (y_diff / 2))]
        elif x_diff == 2:
            return H, [H[0] - 1, H[1]]
        elif x_diff == -2:
            return H, [H[0] + 1, H[1]]
        elif y_diff == 2:
            return H, [H[0], H[1] - 1]
        elif y_diff == -2:
            return H, [H[0], H[1] + 1]
        else:  # still touching
            return H, T

    def move_rope(self, move):
        self.head.pos = [self.head.pos[x] + move[x] for x in range(2)]  # move head
        head = self.head
        # print(f"before move - head:{head.pos} tail:{head.next.pos}")
        while head.next:
            # print(f"head:{head.name} tail:{head.next.name}")
            head.pos, head.next.pos = self.check_moves(head.pos, head.next.pos)
            # print(f"after move - head:{head.pos} tail:{head.next.pos}")
            head = head.next
        return head.pos


H = Knot(name="H")
m1 = Knot(name="m1")
m2 = Knot(name="m2")
m3 = Knot(name="m3")
m4 = Knot(name="m4")
m5 = Knot(name="m5")
m6 = Knot(name="m5")
m7 = Knot(name="m7")
m8 = Knot(name="m8")
T = Knot(name="T")

rope = Rope(H)
rope.append(m1)
rope.append(m2)
rope.append(m3)
rope.append(m4)
rope.append(m5)
rope.append(m6)
rope.append(m7)
rope.append(m8)
rope.append(T)


# print(f"  H       M1      M2      M3      M4      M5      M6      M7      M8      T")
# pprint(rope.get_all_pos())

tail_pos = []
for move in moveset:
    # print(f" ---- {move} ---- ")
    for i in range(move[1]):
        tail_pos.append(rope.move_rope(movement[move[0]]))
        # print(f"{i+1} H       M1      M2      M3      M4      M5      M6      M7      M8      T")
        # pprint(rope.get_all_pos())
    # print(f"end of {move} head at {rope.head.pos} tail at {rope.get_tail().pos}")

unique_pos = []
for p in tail_pos:
    if p not in unique_pos:
        unique_pos.append(p)

print(f"PART 2: num of unique tail position is {len(unique_pos)}")
