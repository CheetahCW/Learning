# -*- coding: utf-8 -*-

import tensorflow as tf


def test_tensor():
    x = [[2., 4., 6.]]
    y = [[1.], [3.], [5.]]
    return tf.multiply(x, y)
