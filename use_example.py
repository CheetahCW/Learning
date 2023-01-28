#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:12:19 2023

@author: Cheetah
"""

import learning.functions.simple as fs
import learning.mydice as dc

x = [-1, 2, 11, -7, 3, 0]
y = fs.range_of_list(x)

dice = dc.RandomGen()
z = dice.next_num()