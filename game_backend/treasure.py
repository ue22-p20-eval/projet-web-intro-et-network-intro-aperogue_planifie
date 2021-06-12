import numpy as np

class Treasure:
    def __init__(self, symbol="T",status='revealed',effect = 'atk+', nb=10):
        self._symbol = symbol
        self.status = status #Hide or revealed
        self._x = None
        self._y = None
        self.nb = nb
        self.effect = effect # Heal+ or Atk+

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

            if y_init > n_row-1 :
                y_init = 0

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol
