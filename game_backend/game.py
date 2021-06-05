from .map_generator import Generator
from .player import Player, Monster
from .treasure import Treasure

class Game:
    def __init__(self, width=64, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level

        self._player = Player()
        self._player.initPos( self._map )

        self._monster = Monster()
        self._monster.initPos( self._map )

        self._treasure = Treasure()
        self._treasure.initPos( self._map )

    def getMap(self):
        return self._map

    def move(self, dx, dy):
        temp1,temp2 = self._player.move(dx, dy, self._map)
        if len(temp1) >0 and temp1[0] == 'Fight required' :
            print("la")
            Game.attack(self,self._player,self._monster)
            if self._monster.alive == False :
                print("la bis")
                self._map[self._player._y + dy][self._player._x + dx] = '.'
                return(self._player.move(dx, dy, self._map))
            else : 
                return([],True)
        else : 
            return (temp1,temp2)
        
    def attack(self,player,monster):
        monster.lp -= player.atk
        if monster.lp < 0 : 
            monster.alive = False 
        else : # Attaque retour 
            player.lp -= monster.atk
            if player.lp <0 :
                player.alive = False