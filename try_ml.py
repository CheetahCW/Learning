#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 18:52:45 2023

@author: Cheetah
"""

import ml.tensor_try as mltf
import ml.torch_try as mlt
import ml.keras_try as kr

import torch
import numpy as np

print(mlt.test_torch())
print(mltf.test_tensor())

normalized_data = kr.normalize_test()
print("\nvar: %.4f" % np.var(normalized_data))
print("mean: %.4f\n" % np.mean(normalized_data))

print(torch.rand(2, 3, 2))
