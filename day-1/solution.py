def getData(input = "input"):
    """
    Retrieves and parses input data from the target file.
    """
    with open(input, "r") as file:
        data = (map(int, line.split()) for line in file)
        left, right = zip(*data)

    return left, right


def part1(left, right):
    """
    Calculates the sum of differences between sorted(l) and sorted(r).
    """
    distances = (abs(x - y) for x, y in zip(left, right))

    return sum(distances)


def part2(left, right):
    """
    Calculates the total similarity score between l and r.
    """
    scores = (x * right.count(x) for x in left)

    return sum(scores)


def main():
    left, right = map(sorted, getData())

    print("Answer 1:", part1(left, right))
    print("Answer 2:", part2(left, right))


if __name__ == "__main__":
    main()
