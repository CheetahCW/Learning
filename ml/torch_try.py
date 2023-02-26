# -*- coding: utf-8 -*-

import torch
import numpy as np


def test_torch():
    x = np.array([[2., 4., 6.]])
    y = np.array([[1.], [3.], [5.]])
    return torch.mul(torch.from_numpy(x), torch.from_numpy(y))
