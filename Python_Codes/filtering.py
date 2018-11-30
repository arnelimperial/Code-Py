#!/usr/bin/env python3
with open("strings.txt", "r") as analyte:
    incubator = analyte.readline()
    analyte.seek(0)
    for incubator in analyte:
        analyzer = incubator.rstrip().isalnum()
        if analyzer:
            print(incubator [:-1], "was ok.")
        else:
            print(incubator[:-1], "was invalid.")
