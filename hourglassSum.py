#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
#
# arr =
#     1 1 1 0 0 0
#     0 1 0 0 0 0
#     1 1 1 0 0 0
#     0 0 0 0 0 0
#     0 0 0 0 0 0
#     0 0 0 0 0 0

# An hourglass A in arr is a subset of values with indices falling in this pattern in arr's graphical representation:

# a b c
#   d
# e f g

TEST_MTX = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [
    19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36]]


def createHourGlasses(rowsList):
    hourGlasses = list()
    i = 0
    while(i+2 < len(rowsList[0])):
        subHourGlasses = [lst[i:i+3] for lst in rowsList]
        subHourGlasses[1] = [subHourGlasses[1][1]]
        hourGlasses.append(
            sum([item for sublist in subHourGlasses for item in sublist]))
        i += 1
    return hourGlasses


def hourglassSum(arr):
    idx_a = 0
    idx_b = 3
    hourGlassesSums = list()
    while(idx_a+2 < len(arr)):
        selectedRows = arr[idx_a:idx_b]
        hourGlassesSums.extend(createHourGlasses(selectedRows))
        idx_a = idx_a + 1
        idx_b = idx_b + 1
    return max(hourGlassesSums)
