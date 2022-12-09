# rope bridge

with open("data/09_smol2.txt") as f:
    moveset = f.readlines()
moveset = [m.strip("\n").split() for m in moveset]
moveset = [(m[0], int(m[1])) for m in moveset]
print(f"total moveset: {moveset}")

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


class RopeNode:
    def __init__(self, pos=[0, 0])  -> None:
        self.pos = pos
        self.next = None


class Rope:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, node) -> None:
        head = self.head
        if head:
            while head.next:
                head = head.next
            head.next = node
        else:
            self.head = node

    def move_rope(self, move):
        head = self.head
            


H = RopeNode()
m1 = RopeNode()
m2 = RopeNode()
m3 = RopeNode()
m4 = RopeNode()
m5 = RopeNode()
m6 = RopeNode()
m7 = RopeNode()
m8 = RopeNode()
T = RopeNode()

long_rope = Rope(H)
