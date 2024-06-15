# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
#
# Input Format
# A single line containing a positive integer, .
#
# Constraints
# 1 <= n <= 100
#
# Output Format
# Print Weird if the number is weird; otherwise, print Not Weird.
#
# Sample Input 0
# 3

# Sample Output 0
# Weird

# Explanation 0
# is odd and odd numbers are weird, so we print Weird.
#


# Sample Input 1
# 24

# Sample Output 1
# Not Weird

# Explanation 1
# n = 24
# n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.


import math
import os
import random
import re
import sys

#!/usr/bin/python


if __name__ == '__main__':
    n = int(input().strip())

    if 1 <= n <= 100 :
        if n % 2 == 1 :
            print("Weird")
        elif n % 2 == 0 :
            if n >=2 & n <= 5 :
                print("Not Weird")
            elif n >=6 & n <=20 :
                print("Weird")
            elif n > 20 :
                print("Not Weird")
    else:
        print("Weird")
        