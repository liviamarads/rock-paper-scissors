#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""
import random

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

def valid_input(prompt):
    while True:
        response = input(prompt).lower()
        if response in moves:
            break
    return response

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class HumanPlayer(Player):
    def move(self):
        return valid_input('Rock, paper, scissors? > ')

class ReflectPlayer(Player):
    lastplayed = 

class Game:
 
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scorep1 = 0
        self.scorep2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 != move2:
            if beats(move1, move2):
                print('** PLAYER ONE WINS **')
                self.scorep1 += 1
            else:
                print('** PLAYER TWO WINS **')
                self.scorep2 += 1
        else: 
            print ('** TIE **')

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
            print(f"Score: Player One {self.scorep1}, Player Two {self.scorep2}") 
        print("Game over!")

if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()