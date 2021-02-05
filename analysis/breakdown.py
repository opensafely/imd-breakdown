import csv
from collections import Counter


CATEGORIES = [0, 1, 2, 3, 4, 5]


def main():
    with open("output/input.csv") as f:
        reader = csv.DictReader(f)
        counter = Counter(imd_category(row["imd"]) for row in reader)

    total = sum(counter.values())

    with open("output/breakdown.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "n", "%"])
        writer.writerows(
            [
                [category, counter[category], f"{100 * counter[category] / total:.1f}"]
                for category in CATEGORIES
            ]
        )


def imd_category(rank):
    if not rank:
        return 0

    rank = int(rank)

    if rank < 1 or rank >= 32844:
        return 0

    for category in CATEGORIES:
        if category == 0:
            continue
        if rank < 32844 * category / 5:
            return category

    assert False, f"Unhandled rank {rank}"


if __name__ == "__main__":
    main()
