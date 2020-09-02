#!/usr/bin/python3

import sys

file_name = sys.argv[1]

with open(file_name, "r") as f:
    for line in f:
        if not line.startswith("!"):
            print("{}".format("".join(line.rstrip().split('\n'))))

