
from src.game import Game

class GameCLI:
    """ A class to represent the Game of Life CLI. 
        This class is responsible for
        running the game and interacting with the user. """

    def __init__(self):
        """ Initialize the GameCLI with an empty board and a Game object. """

        self.board = [[' ' for _ in range(8)] for _ in range(8)]
        self.game = Game(self.board)

    def run(self):
        """ Run the Game of Life CLI. 
            This method will welcome the user, 
            populate the board with living cells, 
            print the board, and simulate the game."""

        print('Welcome to the Game of Life!')
        print('Please populate the board with living cells.')
        self.initialize_board()
        self.game.print_board()
        self.simulate()

    def initialize_board(self):
        """ Initialize the board with living cells. 
            This method will request fromt he user to input the coordinates of living cells. """

        while True:
            x = int(input('Enter the x coordinate of the living cell (0-7): '))
            y = int(input('Enter the y coordinate of the living cell (0-7): '))
            self.board[y][x] = 'X'
            print('Current board:')
            self.game.print_board()
            if input('Do you want to add another living cell? (y/n): ') == 'n':
                break

    def simulate(self):
        """ Simulate the game. 
            This method will request from the user to input the number of rounds to simulate. 
            It will then simulate the game for the chosen number of rounds. """
            
        rounds = int(input('How many rounds would you like to simulate? '))
        for _ in range(rounds):
            self.game.next_generation()
            print('Current board:')
            self.game.print_board()