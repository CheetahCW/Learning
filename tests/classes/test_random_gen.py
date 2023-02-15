#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 15:23:45 2023

@author: Olga Us
"""

import pytest
from learning.classes.random_gen import RandomGen


def test_next_num_is_in_nums():
    in_nums, in_probs = [1, 2, 3], [.2, .3, .5]
    rg = RandomGen(in_nums, in_probs)
    sim = rg.next_num()
    assert sim in in_nums


def test_zero_prob_not_in_nums():
    in_nums, in_probs = [1, 2, 3], [.0, .0, 1.0]
    rg = RandomGen(in_nums, in_probs)
    sim = rg.next_num()
    assert sim == in_nums[2]


def test_single_num_prob():
    in_nums, in_probs = [1], [1.0]
    rg = RandomGen(in_nums, in_probs)
    sim = rg.next_num()
    assert sim == in_nums[0]


def test_probs_sum_to_one():
    in_nums, in_probs = [1, 2, 3], [.2, .3, .0]
    with pytest.raises(ValueError) as exception_info:
        _ = RandomGen(in_nums, in_probs)
    assert exception_info.match('Sum of probabilities must be 1.0')


def test_probs_not_empty():
    in_nums, in_probs = [1, 2, 3], []
    with pytest.raises(ValueError) as exception_info:
        _ = RandomGen(in_nums, in_probs)
    assert exception_info.match('Probabilities cannot be empty')


def test_nums_not_empty():
    in_nums, in_probs = [], [.2, .3, .5]
    with pytest.raises(ValueError) as exception_info:
        _ = RandomGen(in_nums, in_probs)
    assert exception_info.match('Values cannot be empty')


def test_same_dims():
    in_nums, in_probs = [1, 2], [.2, .3, .5]
    with pytest.raises(ValueError) as exception_info:
        _ = RandomGen(in_nums, in_probs)
    assert exception_info.match('Values and probabilities must be of equal sizes')  # noqa : E501


def test_int_nums():
    in_nums, in_probs = [1, 2, 3.5], [.2, .3, .5]
    with pytest.raises(ValueError) as exception_info:
        _ = RandomGen(in_nums, in_probs)
    assert exception_info.match('Values must all be integers')


def test_float_probs():
    in_nums, in_probs = [1, 2, 3], [1, .0, 0]
    with pytest.raises(ValueError) as exception_info:
        _ = RandomGen(in_nums, in_probs)
    assert exception_info.match('Probabilities must all be floats')
