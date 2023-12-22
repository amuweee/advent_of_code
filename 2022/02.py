# rock paper scissors

with open("data/02.txt") as f:
    lines = f.readlines()
    strategy = [l.strip("\n").split(" ") for l in lines]

glossary = {
    "X": "A",  # rock
    "Y": "B",  # paper
    "Z": "C",  # scissors
}


def score(op: str, me: str) -> int:

    match me:
        case "A":  # rock
            match op:
                case "A":  # rock
                    return 1 + 3
                case "B":  # paper
                    return 1 + 0
                case "C":  # scissor
                    return 1 + 6
        case "B":  # paper
            match op:
                case "A":  # rock
                    return 2 + 6
                case "B":  # paper
                    return 2 + 3
                case "C":  # scissor
                    return 2 + 0
        case "C":  # scissor
            match op:
                case "A":  # rock
                    return 3 + 0
                case "B":  # paper
                    return 3 + 6
                case "C":  # scissor
                    return 3 + 3


# part 1
final_score = 0
for strat in strategy:
    op = strat[0]
    me = glossary[strat[1]]
    final_score += score(op, me)
print(f"the total score with inital strategy is: {final_score}")

# part 2
glossary_alt = {
    # win
    "Z": {
        "A": "B",  # rock < paper
        "B": "C",  # paper < scissor
        "C": "A",  # scissor < rock
    },
    # draw
    "Y": {
        "A": "A",
        "B": "B",
        "C": "C",
    },
    # lose
    "X": {
        "A": "C",  # rock > scissor
        "B": "A",  # paper > rock
        "C": "B",  # scissor > paper
    },
}

alt_final_score = 0
for strat in strategy:
    op = strat[0]
    me = glossary_alt[strat[1]][op]
    # print(f"op: {op} outcome: {strat[1]} me: {me} points: {score(op, me)}")
    alt_final_score += score(op, me)
print(f"the total score with alternate strategy is: {alt_final_score}")
