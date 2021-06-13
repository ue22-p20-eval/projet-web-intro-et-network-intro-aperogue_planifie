from .map_generator import Generator
from .player import Player, Monster
from .treasure import Treasure
import numpy as np

class Game:
    def __init__(self, width=64, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level

        self._player = Player()
        self.player2 = Player(symbol='G')
        self._player.initPos( self._map )
        self.M_list = [Monster() for _ in range(np.random.randint(2,6))]
        self.T_list = [Treasure(status='revealed') for _ in range(np.random.randint(3,6)) ]
        
        for monst in self.M_list :
            monst.initPos( self._map )
        for t1 in self.T_list: # Cadeaux apparents
            t1.initPos( self._map )
        
        
        self.T_list[0].effect = 'Heal'#  Le premier cadeau donne toujours de la vie, sinon atk
        self.T_list[-1].status = 'Hide'
        self.T_list[-2].status = 'Hide' 

    def getMap(self):
        return self._map

    def newP(self):
        self.player2.initPos(self._map)
        x,y = self.player2.getpos()
        return(x,y)

    def move(self, dx, dy,player):
        temp1,temp2 = player.move(dx, dy, self._map)
        if len(temp1) >0 and temp1[0] == 'Fight required' :
            ## On recherche sur quel monstre on est tombé :
            i=0
            while not (self.M_list[i]._x == player._x + dx and self.M_list[i]._y == player._y + dy):
                i=i+1

            Game.attack(self,player,self.M_list[i])
            if self.M_list[i].alive == False :
                self._map[player._y + dy][player._x + dx] = '.'
                return(player.move(dx, dy, self._map))
            else : 
                return([],True)
        elif len(temp1)>0 and temp1[0] == 'Fight P1P2' :
            Game.attack(self,player,self.player2)
            return([],True)

        elif len(temp1)>0 and temp1[0] == 'Fight P2P1' :
            Game.attack(self,player,self._player)
            return([],True)

        elif len(temp1) >0 and temp1[0] == 'Treasure found' :
            ## On recherche sur quel trésor on est tombé :
            i=0
            while not (self.T_list[i]._x == player._x + dx and self.T_list[i]._y == player._y + dy):
                i=i+1
            if self.T_list[i].effect == 'Heal':
                player.lp += int(self.T_list[i].nb)
            else :
                player.atk += int(self.T_list[i].nb)
            self._map[player._y + dy][player._x + dx] = '.'
            return(player.move(dx, dy, self._map))

        else : 
            return (temp1,temp2)
        
    def attack(self,player,monster):
        monster.lp -= player.atk
        if monster.lp < 0 : 
            monster.alive = False 
            player.atk += 5
        else : # Attaque retour 
            player.lp -= monster.atk
            if player.lp <=0 :
                player.alive = False