#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = sorted(input().strip())
    c = collections.Counter(s).most_common()
    
    c = sorted(c,key = lambda a : (a[1] * -1, a[0]))
    for i in range(3):
        print(c[i][0],c[i][1])
