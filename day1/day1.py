def part1():
    for num in nums:
        if target - num in nums:
            print("--------- PART 1 ---------")
            print("Answer:", num * (target - num))
            print("Numbers:", num, "and", (target - num))
            return


def part2():
    for i, num in enumerate(nums):
        for num2 in nums[i+1:]:
            for num3 in nums[i+2:]:
                if target == num + num2 + num3:
                    print("\n--------- PART 2 ---------")
                    print("Answer:", num * num2 * num3)
                    print("Numbers:", num, ",", num2, ",", num3)
                    return


if __name__ == "__main__":
    f = open("input.txt", "r")
    nums = [int(i) for i in f.readlines()]
    target = 2020
    part1()
    part2()
