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

        y_initt = np.random.randint(-1,n_row-2)
        found = False
        while found is False:
            y_initt += 1
            if y_initt > n_row -1 :
                y_initt =0
            listT = []
            for i,c in enumerate(_map[y_initt]):
                if c == ".":
                    listT.append(i)

            if len(listT)>0 :
                table = np.array(listT)
                found = True
                np.random.shuffle(table)
                x_initt = table[0]
            

        self._x = x_initt
        self._y = y_initt

        _map[self._y][self._x] = self._symbol
