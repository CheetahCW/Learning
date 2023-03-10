# -*- coding: utf-8 -*-
"""
Machine Learning with Keras
"""

import numpy as np
from tensorflow.keras.layers import Normalization


def normalize_test():
    # Example image data, with values in the [0, 255] range
    training_data = np.random.randint(0, 256, size=(64, 200, 200, 3)).astype("float32")
    normalizer = Normalization(axis=-1)
    normalizer.adapt(training_data)
    return normalizer(training_data)
    print("var: %.4f" % np.var(normalized_data))
    print("mean: %.4f" % np.mean(normalized_data))