#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:12:19 2023

@author: Cheetah
"""

#import learning.functions.simple as fs
import learning.mydice as dc
#import numpy as np
#import random
import time

start_time = time.time()
#x = [-1, 2, 11, -7, 3, 0]
#y = fs.range_of_list(x)

dice = dc.RandomGen()
#z = dice.next_num()

#inprobs = np.array([.1, .2, .3, .4])
#vals = np.array([10, 20, 30, 40])
#inprobs_cum = np.cumsum(inprobs)
#inprobs_cum_new = np.insert(inprobs_cum, 0, 0)

#Alist = []
total = 10000
#for i in range(0, total):
#    idx = np.where(inprobs_cum <= random.random())
#    idx = np.digitize(random.random(), inprobs_cum_new, True)
#    val_found = vals[len(*idx)]
#    val_found = vals[idx - 1]
#    val_found = dice.next_num()
#    Alist.append(val_found)

Alist = [dice.next_num() for _ in range(total)]
outprobs = {x: Alist.count(x)/total for x in Alist}

#x = random.random()
#idx_new = np.digitize(x, inprobs_cum_new, True)
#val_new = vals[idx_new - 1]
print("--- %s seconds ---" % (time.time() - start_time))