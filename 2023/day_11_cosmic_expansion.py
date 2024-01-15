import itertools

with open("data/11.txt") as f:
    data = f.readlines()
    data = [d.strip("\n") for d in data]


def helper_viz_sky(sky: list[str]) -> None:
    for row in sky:
        print(row)


def add_empty_space(data: list[str]) -> list[str]:
    new_rows = []
    for row in data:
        if "#" in set(row):
            new_rows.append(row)
        else:
            new_rows.append(row)
            new_rows.append(row)
    return new_rows


def rotate(sky: list[str]) -> list[str]:
    rotated = list(zip(*sky[::-1]))
    sky = []
    for row in rotated:
        sky.append("".join(row))
    return sky


def expand_cosmic_sky(data: list[str]) -> list[str]:
    expanded_row = add_empty_space(data)
    rotated = rotate(expanded_row)
    expanded_col = add_empty_space(rotated)
    rotated = rotate(expanded_col)
    rotated = rotate(rotated)
    rotated = rotate(rotated)

    return rotated


def create_galaxy_index(sky: list[str]) -> dict[str, tuple[int, int]]:
    galaxy_index = {}
    galaxy_counter = 1
    for x, row in enumerate(sky):
        for y, spot in enumerate(row):
            if spot == "#":
                galaxy_index[str(galaxy_counter)] = (x, y)
                galaxy_counter += 1

    return galaxy_index


def count_distance_between_galaxies(
    galaxy_a: tuple[int, int], galaxy_b: tuple[int, int]
) -> int:
    x_distance = abs(galaxy_a[0] - galaxy_b[0])
    y_distance = abs(galaxy_a[1] - galaxy_b[1])
    return x_distance + y_distance


def solve_part_1(data: list[str]) -> int:
    sky = expand_cosmic_sky(data)
    galaxy_index = create_galaxy_index(sky)

    all_galaxies = list(galaxy_index.keys())
    unique_pairs = list(itertools.combinations(all_galaxies, 2))
    all_distances = 0
    for pairs in unique_pairs:
        all_distances += count_distance_between_galaxies(
            galaxy_index[pairs[0]], galaxy_index[pairs[1]]
        )

    print(f"Part 1: {all_distances}")
    return all_distances


def find_empty_spaces_in_sky(sky: list[str]) -> list[list[int]]:
    x_empty = []
    y_empty = []
    for i, row in enumerate(sky):
        if "#" not in set(row):
            x_empty.append(i)
    rotated_sky = rotate(sky)
    for i, row in enumerate(rotated_sky):
        if "#" not in set(row):
            y_empty.append(i)

    return [x_empty, y_empty]


def custom_galaxy_expansion_counter(sky: list[str], expansion: int) -> int:
    galaxy_index = create_galaxy_index(sky)
    all_galaxies = list(galaxy_index.keys())
    unique_pairs = list(itertools.combinations(all_galaxies, 2))
    all_distances = 0

    empty_spaces = find_empty_spaces_in_sky(sky)

    def count_distance_between_galaxies(
        galaxy_a: tuple[int, int],
        galaxy_b: tuple[int, int],
        empty_spaces: list[list[int]],
        expansion: int,
    ) -> int:
        x_distance = abs(galaxy_a[0] - galaxy_b[0])
        gap_x = sorted([galaxy_a[0], galaxy_b[0]])
        for i in range(gap_x[0], gap_x[1] + 1):
            if i in empty_spaces[0]:
                x_distance += expansion - 1

        y_distance = abs(galaxy_a[1] - galaxy_b[1])
        gap_y = sorted([galaxy_a[1], galaxy_b[1]])
        for i in range(gap_y[0], gap_y[1] + 1):
            if i in empty_spaces[1]:
                x_distance += expansion - 1
        return x_distance + y_distance

    for pairs in unique_pairs:
        all_distances += count_distance_between_galaxies(
            galaxy_index[pairs[0]], galaxy_index[pairs[1]], empty_spaces, expansion
        )

    return all_distances


def solve_part_2(data: list[str]) -> int:
    distances = custom_galaxy_expansion_counter(data, 1000000)
    print(f"Part 2: {distances}")
    return distances


if __name__ == "__main__":
    solve_part_1(data)
    solve_part_2(data)
