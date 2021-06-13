import numpy as np
class Player:
    def __init__(self, lp=100, atk=5,symbol="@"):
        self._symbol = symbol
        self.lp = lp #Life point
        self.atk = atk
        self._x = None
        self._y = None
        self.alive = True

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_initp = np.random.randint(-1,n_row-2)
        found = False
        while found is False:
            y_initp += 1
            if y_initp > n_row -1 :
                y_initp =0
            listP = []
            for i,c in enumerate(_map[y_initp]):
                if c == ".":
                    listP.append(i)

            if len(listP)>0 :
                table = np.array(listP)
                found = True
                np.random.shuffle(table)
                x_initp = table[0]
            

        self._x = x_initp
        self._y = y_initp

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
            ret = True
            data = ['Fight required']
        elif map[new_y][new_x] == "T":
            ret = True
            data = ['Treasure found']
        else:
            ret = False
            data = []
        return data, ret
    def getpos(self):
        return(self._x,self._y)
    


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

        y_initm = np.random.randint(-1,n_row-2)
        found = False
        while found is False:
            y_initm += 1
            if y_initm > n_row -1 :
                y_initm =0
            listM = []
            for i,c in enumerate(_map[y_initm]):
                if c == ".":
                    listM.append(i)

            if len(listM)>0 :
                table = np.array(listM)
                found = True
                np.random.shuffle(table)
                x_initm = table[0]
            

        self._x = x_initm
        self._y = y_initm

        _map[self._y][self._x] = self._symbol