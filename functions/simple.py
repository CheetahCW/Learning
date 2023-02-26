#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Learning simple functions
"""


def list_range(x):
    """ Difference between its max and min """
    return max(x) - min(x)


def list_range_abs(x):
    """ Difference between its abs max and abs min """
    return list_range([abs(k) for k in x])


def list_reversed(x):
    """ Return a reversed list """
    return x[::-1]


def list_add_value(x, a):
    """ Add value 'a' to all elements"""
    return [k + a for k in x]


def list_mod_only(x, a):
    """ Return elements % a """
    return [k for k in x if k % a == 0]


def list_merge(x, y):
    """ Return pairs from each list """
    return list(zip(x, y))


def list_to_dict(x, y):
    """ Returns a dictionary made of two lists """
    return dict(zip(x, y))
