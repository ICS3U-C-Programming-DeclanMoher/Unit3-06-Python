#!/usr/bin/env python3
import random


def main():
    # generate a random number 0-9
    random_variable = random.randint(0, 9)

    # get user number as a string
    integer_as_string = input("Enter an integer:")
    print("")

    # going to check if input is correct
    try:
        # covert from string into int
        integer_as_number = int(integer_as_string)
        print("you entered a integer correctly")

    #
    except Exception:
        print("you entered a integer incorrectly")

    # going to tell you what number you put in
    finally:
        print("thank for playing ")


if __name__ == "__main__":
    main()
