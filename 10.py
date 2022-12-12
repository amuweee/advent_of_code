# cathode ray tube
from pprint import pprint
from collections import deque

with open("data/10.txt") as f:
    signals = f.readlines()
    signals = [l.strip("\n") for l in signals]

class CPU:
    def __init__(self) -> None:
        self.cycle = 1
        self.x = 1
        self.queue = deque()
        self.outputs = []

    def save_output(self):
        self.outputs.append((self.cycle, self.x, self.cycle * self.x, list(self.queue)))

    def run_cycle(self, signal):

        # import pdb; pdb.set_trace()

        if len(self.queue) != 0:
            while len(self.queue) != 0:
                self.save_output()
                self.x += self.queue.popleft()
                self.cycle += 1

        match signal.split():
            case ["noop"]:
                self.save_output()
                self.cycle += 1
            case ["addx", val]:
                self.queue.append(int(val))
                self.save_output()
                self.cycle += 1


cpu = CPU()
for sig in signals:
    cpu.run_cycle(sig)

# pprint(cpu.outputs)
o = [a for a in cpu.outputs if a[0] in [20, 60, 100, 140, 180, 220]]
# pprint(o)
print(f"PART 1 SUM IS {sum([a[2] for a in o])}")


# part deux
