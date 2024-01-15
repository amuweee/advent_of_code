from dataclasses import dataclass

with open("data/10.txt") as f:
    data = f.readlines()

"""
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""

moves = {
    "north": [-1, 0],
    "south": [1, 0],
    "east": [0, 1],
    "west": [0, -1],
}

connections_dict = {
    "|": [moves["north"], moves["south"]],
    "-": [moves["east"], moves["west"]],
    "L": [moves["north"], moves["east"]],  # north, east
    "J": [moves["north"], moves["west"]],  # north, west
    "7": [moves["south"], moves["west"]],  # south, west
    "F": [moves["south"], moves["east"]],  # south, east
}


def parse_map_to_2d_array(data: list[str]) -> list[list[str]]:
    grid = []
    for line in data:
        grid.append([a for a in line.strip("\n")])
    return grid


@dataclass
class Pipe:
    position_x: int
    position_y: int
    position_str: str
    shape: str
    distance: int = 0

    def find_connected_pipes(self) -> list[str]:
        self.connected_pipes_pos = []
        if self.shape == "." or self.shape == "S":
            return self.connected_pipes_pos
        moves = connections_dict[self.shape]
        for m in moves:
            self.connected_pipes_pos.append(
                str(self.position_x + m[0]) + "." + str(self.position_y + m[1])
            )
        return self.connected_pipes_pos


def pipes_constructor(data: list[list[str]]) -> list[Pipe]:
    pipes_list = []
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            pipe = Pipe(
                position_x=x,
                position_y=y,
                position_str=str(x) + "." + str(y),
                shape=char,
            )
            pipe.find_connected_pipes()
            pipes_list.append(pipe)

    return pipes_list


def convert_pipes_list_to_pipe_index(pipes_list: list[Pipe]) -> dict[str, Pipe]:
    pipe_index = {pipe.position_str: pipe for pipe in pipes_list}
    return pipe_index


def add_distance_from_start(pipe_index: dict[str, Pipe]) -> dict[str, Pipe]:
    start_loc = [loc for loc, pipe in pipe_index.items() if pipe.shape == "S"][0]
    length = 0
    counted_pipes = set(
        loc
        for loc, pipe in pipe_index.items()
        if pipe.shape == "." or pipe.shape == "S"
    )
    connected = [
        loc for loc, pipe in pipe_index.items() if start_loc in pipe.connected_pipes_pos
    ]
    # print(f"starting vals {connected=}, {counted_pipes=}")
    next_pipes = []

    while len([c for c in connected if c not in counted_pipes]) > 0:
        length += 1
        for i in range(len(connected)):
            # print(f"loop {connected[i]} of {connected}: {length=}")
            current_pipe = pipe_index[connected[i]]
            current_pipe.distance = length
            counted_pipes.add(current_pipe.position_str)
            counted_pipes = set(counted_pipes)
            next_pipes += current_pipe.connected_pipes_pos
        connected = list(set(next_pipes))[:]
        connected = [c for c in connected if c not in counted_pipes]
        # print(f"{len(counted_pipes)=}")
        # print(f"{20*'-'}")

    return pipe_index


def construct_pipes_with_distances(data: list[str]) -> dict[str, Pipe]:
    pipes_array = parse_map_to_2d_array(data)
    all_pipes = pipes_constructor(pipes_array)
    pipe_index = convert_pipes_list_to_pipe_index(all_pipes)
    pipes_with_distances = add_distance_from_start(pipe_index)

    return pipes_with_distances


def solve_part_1(pipe_index: dict[str, Pipe]) -> int:
    farthest = max([pipe.distance for pipe in pipe_index.values()])
    longest_pipes_from_start = [
        pipe for pipe in pipe_index.values() if pipe.distance == farthest
    ]

    for pipe in longest_pipes_from_start:
        if (
            pipe_index[pipe.connected_pipes_pos[0]].distance == farthest - 1
            and pipe_index[pipe.connected_pipes_pos[1]].distance == farthest - 1
        ):
            print(f"Part 1: {pipe.distance}")
            return pipe.distance

    return 0


def helper_viz_draw_loop_with_box(pipe_index: dict[str, Pipe]) -> dict[str, Pipe]:
    box_drawings = {
        "L": "└",
        "J": "┘",
        "7": "┐",
        "F": "┌",
    }
    for loc, pipe in pipe_index.items():
        if pipe.shape != "S" and pipe.distance == 0:
            pipe_index[loc].shape = "."
        else:
            pipe_index[loc].shape = box_drawings.get(pipe.shape, pipe.shape)
    max_x = max([pipe.position_x for pipe in pipe_index.values()]) + 1
    max_y = max([pipe.position_y for pipe in pipe_index.values()]) + 1
    for x in range(max_x):
        string = ""
        x_pipes = [pipe for pipe in pipe_index.values() if pipe.position_x == x]
        x_pipes_dict = {pipe.position_y: pipe.shape for pipe in x_pipes}
        for y in range(max_y):
            string += x_pipes_dict[y]
        print(string)

    return pipe_index


def find_area_inside_drawn_polygon(pipe_index: dict[str, Pipe]) -> int:
    # shoelace formula
    start = [pipe for pipe in pipe_index.values() if pipe.shape == "S"][0]
    turning_points = [(start.position_x, start.position_y)]
    connected = []
    return 100

def solve_part_2(pipe_index):
    return 0


if __name__ == "__main__":
    pipe_index = construct_pipes_with_distances(data)
    pipe_index_viz = helper_viz_draw_loop_with_box(pipe_index)
    solve_part_1(pipe_index)
