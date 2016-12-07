#!/usr/bin/env python3
from random import randint

class Player(object):
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.score = 0
    def incrementScore(self):
        self.score = self.score + 1

class RockPaperScissors(object):
    def __init__(self, player1, player2):
        super(RockPaperScissors, self).__init__()
        self.player1 = player1
        self.player2 = player2
        self.gameEnd = False
        self.winner = False
        self.moves = ['rock', 'paper', 'scissors']

    def announceWinner(self):
        print('{name} has won the game. score: {score}'.format(name=self.winner.name,
            score= self.winner.score
        ))
    def start(self):
        while not self.gameEnd:
            p1Moves = self.moves[randint(0,2)]
            p2Moves = self.moves[randint(0,2)]
            if(p1Moves == p2Moves):
                print('Tie!')
            elif (p1Moves == 'rock' and p2Moves == 'scissors'):
                print('p1 wins');
                self.player1.incrementScore()
            elif (p1Moves == 'scissors' and p2Moves == 'paper'):
                print('p1 wins');
                self.player1.incrementScore()
            elif (p1Moves == 'paper' and p2Moves == 'rock'):
                print('p1 wins');
                self.player1.incrementScore()
            else:
                print('p2 wins');
                self.player2.incrementScore()

            if(self.player1.score == 3):
                self.winner = self.player1
                self.gameEnd = True
                self.announceWinner()
            if(self.player2.score == 3):
                self.winner = self.player2
                self.gameEnd = True
                self.announceWinner()




p1 = Player('p1')
p2 = Player('p2')

prc = RockPaperScissors(p1, p2)

prc.start()
