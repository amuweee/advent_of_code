import itertools
import math

with open("data/08.txt") as f:
    data = f.readlines()


instructions = data[0].strip("\n")
all_network = data[2:]


class Node:
    def __init__(self, node_string: str) -> None:
        strings = node_string.split()
        self.location: str = strings[0]
        self.location_suffix: str = strings[0][-1]
        self.right: str = strings[-1][:3]
        self.left: str = strings[-2][1:4]
        self.right_suffix: str = strings[-1][:3][-1]
        self.left_suffix: str = strings[-2][1:4][-1]

    def __repr__(self) -> str:
        return f"loc:{self.location} l:{self.left} r:{self.right}"

    def find_next(self, direction: str) -> str:
        if direction == "L":
            return self.left
        elif direction == "R":
            return self.right
        else:
            return "???"

    def find_next_suffix(self, direction: str) -> str:
        if direction == "L":
            return self.left_suffix
        elif direction == "R":
            return self.right_suffix
        else:
            return "???"


def create_network_dict(network_strings: list[str]) -> dict[str, Node]:
    network_dict = {}
    for network in network_strings:
        node = Node(network)
        network_dict[node.location] = node

    return network_dict


def find_next_node(network_dict: dict[str, Node], location: str, direction: str) -> str:
    return network_dict[location].find_next(direction)


def solve_part_1(instructions: str, all_network: list[str]) -> int:
    step_counter = 0
    current_node = "AAA"
    endless_ins = itertools.cycle(instructions)
    network = create_network_dict(all_network)
    for ins in endless_ins:
        if current_node == "ZZZ":
            break
        else:
            step_counter += 1
            current_node = network[current_node].find_next(ins)

    print(f"Part 1: {step_counter}")
    return step_counter


def solve_part_2(instructions: str, all_network: list[str]) -> int:
    all_steps = []
    network = create_network_dict(all_network)

    current_nodes = [node for node in network.values() if node.location_suffix == "A"]
    # just do LCM..
    for node in current_nodes:
        step_counter = 0
        for ins in itertools.cycle(instructions):
            if node.location_suffix == "Z":
                all_steps.append(step_counter)
                break
            else:
                step_counter += 1
                node = network[network[node.location].find_next(ins)]

    lcm = math.lcm(*all_steps)
    print(f"Part 2: {lcm}")
    return lcm


if __name__ == "__main__":
    solve_part_1(instructions, all_network)
    solve_part_2(instructions, all_network)
