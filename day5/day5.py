import math

def get_seat_numbers(seat):
    seat = seat.replace('F', 0).replace('B', 1).replace()


if __name__ == "__main__":
    f = open("input.txt", "r")
    seat_binary = f.read().split("\n")

    print("---------- PART 1 ----------")
    print(get_seat_numbers("FBFBBFFRLR"))

    print("---------- PART 2 ----------")
