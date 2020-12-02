def part1():
    valid = 0
    for entry in passwords:
        instances = entry[0]
        char = entry[1]
        password = entry[2]

        if instances[0] <= password.count(char) <= instances[1]:
            valid += 1

    print("---------- PART 1 ----------")
    print(valid, "valid passwords found.")


def part2():
    valid = 0
    for entry in passwords:
        pos = entry[0]
        char = entry[1]
        password = entry[2]

        if password[pos[0]-1] == char and password[pos[1]-1] != char:
            valid += 1
        elif password[pos[0]-1] != char and password[pos[1]-1] == char:
            valid += 1

    print("\n---------- PART 2 ----------")
    print(valid, "valid passwords found.")


if __name__ == "__main__":
    passwords = []
    with open("input.txt", "r") as f:
        lines = f.read().splitlines()
        for line in [l.split(' ') for l in lines]:
            passwords.append(
                [[int(x) for x in line[0].split('-')],
                 line[1][:-1],
                 line[2]])

    part1()
    part2()
