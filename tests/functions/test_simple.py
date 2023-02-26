# -*- coding: utf-8 -*-
"""
Tests for learning/functions/simple.py

"""

import pytest
import learning.functions.simple as fs


def test_list_range():
    assert fs.list_range([-1, -10, 2, 5, 0]) == 15
    assert fs.list_range([5]) == 0


@pytest.mark.parametrize("list_in, val_out", [
    ([-1, -10, 2, 5, 0], 10),
    ([.1, .2, -.5, 1.7], 1.6),
    ([-1, 1], 0),
])
def test_list_range_abs_mark(list_in, val_out):
    assert fs.list_range_abs(list_in) == pytest.approx(val_out)


# def test_list_range_abs():
#    assert fs.list_range_abs([-1, -10, 2, 5, 0]) == 10
#    assert fs.list_range_abs([.1, .2, -.5, 1.7]) == 2.2
#    assert fs.list_range_abs([-1, 1]) == 0


@pytest.mark.skip(reason="Test skip w/marker")
def test_list_reversed():
    assert fs.list_reversed([1, 15, 25]) == [25, 15, 1]


def test_list_add_value():
    assert fs.list_add_value([5, 2, -2], -2) == [3, 0, -4]


def test_list_mod_only():
    assert fs.list_mod_only([1, -3, 9, 77, 81], 3) == [-3, 9, 81]


def test_list_merge():
    assert fs.list_merge([1, 2, 3], [5, 6, 7]) == [(1, 5), (2, 6), (3, 7)]


def test_list_to_dict():
    assert fs.list_to_dict([1, 2, 3], ['a', 'b', 'c']) == \
                            {1: 'a', 2: 'b', 3: 'c'}
