from json import load

INPUT_FILENAME = "input.json"


def task() -> float:
    with open(INPUT_FILENAME, 'r', encoding="utf-8") as src:
        data = load(src)

    product = sum(record["score"] * record['weight']
                  for record in data)
    return round(product, 3)


print(task())
