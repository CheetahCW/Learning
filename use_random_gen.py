# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 23:12:19 2023

"""


import classes.random_gen as rg


# def main():

in_nums = [10, 20, 30, 40, 50, 60]
in_probs = [.1, .2, .3, .2, .15, .05]

my_rnd = rg.RandomGen(in_nums, in_probs)

total = 10000

Alist = [my_rnd.next_num() for _ in range(total)]
out_probs = {x: Alist.count(x)/total for x in Alist}

in_dict = {in_nums[i]: in_probs[i] for i in range(len(in_nums))}
for num in out_probs.keys():
    out_probs[num] = [out_probs[num]]
    out_probs[num].append(in_dict[num])

print(out_probs)


# if __name__ == "__main__":
#     main()
