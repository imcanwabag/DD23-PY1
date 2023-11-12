from csv import DictReader
from json import dump


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r", encoding="utf-8") as file:
        reader = DictReader(file)
        records = list(reader)

    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as file:
        dump(records, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
