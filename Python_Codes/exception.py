#!/usr/bin/env python3

import sys, os

def int_tester(int_entry):

    try:
        int_entry = int(input("Give a number:"))

    except Exception:
        print("The input was malformed.")
    else:
        print("The input was suitable!")


if __name__ == "__main__":
    int_tester(str)
