
from utilities.logger import log_function_call

class Game:
    """ A class to represent the Game of Life. 
        This class is responsible for
        simulating the game and calculating the next generation of cells. """

    @log_function_call
    def __init__(self, board):
        self.board = board

    @log_function_call
    def print_board(self):
        for row in self.board:
            print(''.join(row))

    @log_function_call
    def next_generation(self):
        """ Calculate the next generation of cells.
            This method will calculate the next generation of cells
            according to the rules of the game of life. """

        new_board = []
        for i in range(len(self.board)):
            new_row = []
            for j in range(len(self.board[i])):
                new_row.append(self.get_new_cell_state(i, j))
            new_board.append(new_row)
        self.board = new_board

    @log_function_call
    def get_new_cell_state(self, i, j):
        """ Get the new state of a cell.
            This method will return the new state of a cell
            according to the rules of the game of life. 
            - A living cell with less than two living neighbors dies.
            - A living cell with two or three living neighbors lives. """

        live_neighbors = self.count_live_neighbors(i, j)
        if self.board[i][j] == 'X':
            if live_neighbors < 2 or live_neighbors > 3:
                return ' '
            return 'X'
        else:
            if live_neighbors == 3:
                return 'X'
            return ' '

    @log_function_call
    def count_live_neighbors(self, i, j):
        """ Count the number of living neighbors of a cell.
            This method will count the number of living neighbors of a cell. """

        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                if 0 <= i + x < len(self.board) and 0 <= j + y < len(self.board[i]):
                    if self.board[i + x][j + y] == 'X':
                        count += 1
        return count
    