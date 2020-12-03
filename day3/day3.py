def part1(slope):
    row_len = len(field[0])
    trees = 0
    x = 0
    for y in range(slope[0], len(field), slope[0]):
        row = field[y]
        x = (x + slope[1]) % row_len
        if row[x] is '#':
            trees += 1
    return trees


def part2(slopes):
    total = 1
    for slope in slopes:
        total *= part1(slope)

    return total


if __name__ == "__main__":
    f = open("input.txt", "r")
    field = f.read().split("\n")
    print("---------- PART 1 ----------")
    print(part1([1, 3]), "trees.")

    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    print("---------- PART 2 ----------")
    print(part2(slopes))
