#!/usr/bin/env python3

# exercise 1
class Player(object):
    """docstring for Player."""
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.x = x
        self.y = y

player1 = Player(34, 45)
player2 = Player(30, 23)
player3 = Player(12, 55)

# exercise 2
class Position(object):
    """docstring for Postion."""
    def __init__(self, x, y):
        super(Position, self).__init__()
        self.x = x
        self.y = y

position1 = Position(120, 234)
position2 = Position(123, 433)
position3 = Position(93, 234)

#exercise 3
class Player(object):
    """docstring for Player."""
    def __init__(self, pos):
        super(Player, self).__init__()
        self.position = pos

player1 = Player(Position(34, 45))
player2 = Player(Position(30, 23))
player3 = Player(Position(12, 55))

#exercise 4

class Game(object):
    """docstring for Game."""
    def __init__(self, title, player1, player2):
        super(Game, self).__init__()
        self.title = title
        self.player1 = player1
        self.player2 = player2

game = Game('rock paper scissors', 'p1', 'p2')
