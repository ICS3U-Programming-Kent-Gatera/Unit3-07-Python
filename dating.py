#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Oct 19
# This program checks if a user is eligible to date someone's grandkid.


def main():
    romance = True
    while romance == True:
        user_age = input("What is the user age?: ")
        try:
            int_user_age = int(user_age)
            if int_user_age >= 25 and int_user_age < 40:
                print("You can date Grandma Babushka's grandchild")
                romance = False
            else:
                print("You are not in the right demographic.")
        except Exception:
            print("Invaid age")
            romance = False


if __name__ == "__main__":
    main()
