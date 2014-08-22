#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  10.py
#  

import itertools

def next_morris(number):
    return ''.join('%s%s' % (len(list(group)), digit)
                   for digit, group in itertools.groupby(str(number)))

def morris_generator(solve_for):
    num = 1
    while num < solve_for:
        yield int(num)
        num = next_morris(num)
		
for n in morris_generator(1000000):
    print(n)

