"""Random numbers for an uneven dice roll."""import randomimport numpy as npclass RandomGen():    _random_nums = [1, 2, 3, 4, 5, 6]    _probabilities = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]        def __init__(self):        self._cumprobs = np.cumsum(self._probabilities)        def next_num(self):        rnd = random.random()        return rnd