with open("data/06.txt") as f:
    data = f.readlines()


def parse_inputs(lines: list[str]) -> list[tuple[int, int]]:
    time = []
    distance = []
    for line in lines:
        line = line.split()
        if line[0] == "Time:":
            time += [int(i) for i in line if i.isdigit()]
        elif line[0] == "Distance:":
            distance += [int(i) for i in line if i.isdigit()]
    races = list(zip(time, distance))
    return races


def calculate_score(time: int, hold: int) -> int:
    time_remaining = time - hold
    velocity = hold
    score = velocity * time_remaining

    return score


def answer_part1(data: list[str]) -> int:
    winning_scores = 1
    races = parse_inputs(data)
    for race in races:  # (7, 9)
        win_count = 0
        time, record = race
        for hold in range(time):
            if calculate_score(time, hold) > record:
                win_count += 1
        winning_scores *= win_count

    return winning_scores

def parse_input_w_kerning(lines: list[str]) -> list[int]:
    time = int("".join([i for i in lines[0].split() if i.isdigit()]))
    distance = int("".join([i for i in lines[1].split() if i.isdigit()]))
    race = [time, distance]
    return race


def get_holding_time_thresholds(time:int, distance: int) -> int:
    thresholds = 0
    for t in range(0, time + 1):
        score = calculate_score(time, t)
        # print(f"{t=}, {time=}, {score=}")
        if score > distance:
            thresholds += time - t
            # print(f"{thresholds=}")
            break
    for i, t in enumerate(range(time, -1, -1), 1):
        score = calculate_score(time, i)
        # print(f"{i=}, {t=}, {time=}, {score=}")
        if score > distance:
            thresholds += - i + 1
            # print(f"{thresholds=}")
            break
    return thresholds


def answer_part2(data: list[str]) -> int:
    time, distance = parse_input_w_kerning(data)
    winning_scores = get_holding_time_thresholds(time, distance)
    return winning_scores

if __name__ == "__main__":
    part_one = answer_part1(data)
    print(part_one)
    part_two = answer_part2(data)
    print(part_two)
