import numpy as np

class Treasure:
    def __init__(self, symbol="T",status='hide'):
        self._symbol = symbol
        self._status = status #Hide or revealed
        self._x = None
        self._y = None

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = np.random.randint(n_row)
        found = False
        while found is False:
            for i,c in enumerate(_map[y_init]):
                if c == ".":
                    x_init = i
                    found = True
                    break
            y_init += 1

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol