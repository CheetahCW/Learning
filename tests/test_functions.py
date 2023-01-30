# -*- coding: utf-8 -*-
"""
Tests for learning/functions/

"""

from learning.functions.simple import range_of_list

def test_range_of_list():
    assert range_of_list([-1, -10, 2, 5, 0]) == 15