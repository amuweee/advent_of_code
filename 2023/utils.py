def open_file(text_file: str) -> list[str]:
    with open(f"data/{text_file}.txt") as f:
        data = f.readlines()
        data = [d.strip("\n") for d in data]
    return data
