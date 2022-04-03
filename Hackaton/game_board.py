import string
import pygame
import ship

alphabet = [letter for letter in string.ascii_uppercase]
numbers = [i + 1 for i in range(26)]
  
class Board():
    def __init__(self, size = 8):
        self.size = size
        self.board = {}
        for letter in alphabet[:self.size]:
            for num in numbers[:self.size]:
                self.board[letter + str(num)] = 0
    
    def extend_ship(self, ship):
        if ship in list(self.board.values()):
            idx = list(self.board.values()).index(ship)
            
    def check_overlap(self):
        values = list(self.board.values())
        new_values = []
        for i in range(-1, self.size + 1, 1):
            new_values.append([])
            for j in range(-1, self.size + 1, 1):
                if i == -1 or j == -1 or i == self.size or j == self.size:
                    new_values[i + 1].append(0)
                else:
                    new_values[i + 1].append(values[self.size * i + j])
        
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if new_values[i][j] != 0:
                    neigbours = [new_values[i - 1][j -1], \
                                new_values[i - 1][j], \
                                new_values[i - 1][j + 1], \
                                new_values[i][j -1], \
                                new_values[i][j + 1], \
                                new_values[i + 1][j -1], \
                                new_values[i + 1][j], \
                                new_values[i + 1][j + 1]]
                        
                    if any(neigbours):
                        return True
        return False
                    
    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                grid_name = list(self.board.keys())[self.size * i + j]
                grid_value = str(list(self.board.values())[self.size * i + j])
                print(grid_name + " " + grid_value, end = "| ")
            print("\n" + "______" * self.size)

b = Board()
