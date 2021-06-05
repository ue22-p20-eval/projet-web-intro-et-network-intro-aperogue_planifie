import numpy as np
class Player:
    def __init__(self, lp=100, atk=10,symbol="@"):
        self._symbol = symbol
        self.lp = lp #Life point
        self.atk = atk
        self._x = None
        self._y = None
        self.alive = True

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == ".":
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy

        if map[new_y][new_x] == "." or map[new_y][new_x] == "x" :
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "x"
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"x"}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}]
            self._x = new_x
            self._y = new_y
        elif map[new_y][new_x ] == "M":
            print("player -> M ")
            ret = True
            data = ['Fight required']
        else:
            ret = False
            data = []
        return data, ret
    


class Monster:
    def __init__(self,lp=10,atk=10,symbol="M"):
        self._symbol = symbol
        self.lp = lp
        self._x = None
        self._y = None
        self.atk = atk
        self.alive = True

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

            if y_init > n_row :
                y_init = 1

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol 