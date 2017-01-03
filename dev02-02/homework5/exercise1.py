#!/usr/bin/env python3

class Player(object):
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.healthpoints = 10
    def Heal(self):
        self.healthpoints = self.healthpoints + 1
    def Damage(self):
        self.healthpoints = self.healthpoints -1


class Game(object):
    def __init__(self, player1, player2):
        super(Game, self).__init__()
        self.player1 = player1
        self.player2 = player2
    def Cheat(self):
        self.player1.Heal()
        self.player2.Damage()

p1 = Player('p1')
p2 = Player('p2')

game = Game(p1, p2)

game.Cheat()
