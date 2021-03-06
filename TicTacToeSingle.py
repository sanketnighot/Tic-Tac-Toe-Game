import os
import random

os.system("cls")


class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(" ")
        print("            %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3],))
        print("           -----------")
        print("            %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6],))
        print("           -----------")
        print("            %s | %s | %s " % (self.cells[7], self.cells[8], self.cells[9],))
        print(" ")

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        for combo in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result:
                return True
        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def reset(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def ai_move(self, player):
        # Choose Center if open
        if self.cells[5] == " ":
            self.update_cell(5, player)
            return

        # AI Wins

        for i in [1, 2, 3]:
            if self.cells[i] == player and self.cells[i + 3] == player and self.cells[i + 6] == " ":
                return i + 6
            if self.cells[i + 3] == player and self.cells[i + 6] == player and self.cells[i] == " ":
                return i
            if self.cells[i] == player and self.cells[i + 6] == player and self.cells[i + 3] == " ":
                return i + 3
            if self.cells[i] == player and self.cells[i + 2] == player and self.cells[i + 3] == " ":
                return i + 3
            if self.cells[i] == player and self.cells[i + 3] == player and self.cells[i + 6] == " ":
                return i + 6
            if self.cells[i + 3] == player and self.cells[i + 6] == player and self.cells[i] == " ":
                return i
            if self.cells[i] == player and self.cells[i + 6] == player and self.cells[i + 3] == " ":
                return i + 3
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == " ":
            return 9
        if self.cells[5] == player and self.cells[9] == player and self.cells[1] == " ":
            return 1
        if self.cells[9] == player and self.cells[1] == player and self.cells[5] == " ":
            return 5
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == " ":
            return 7
        if self.cells[5] == player and self.cells[7] == player and self.cells[3] == " ":
            return 3
        if self.cells[7] == player and self.cells[3] == player and self.cells[5] == " ":
            return 5




        # AI Blocks

        # Choose Random

        while True:
            rint = random.randint(1, 9)
            if self.cells[rint] == " ":
                self.update_cell(rint, player)
                return


board = Board()


def print_header():
    print("WelCome to 'TIc - TAc - TOe'\n")


def refresh_screen():
    # Clear the screen
    os.system("cls")

    # Print Header
    print_header()

    # Display Board
    board.display()


refresh_screen()

while True:
    refresh_screen()

    # Get X input
    x_choice = int(input("\n Player 'X', Choose from 1 - 9 >>> "))

    # Update Board
    board.update_cell(x_choice, "X")

    refresh_screen()
    # Check for X wins
    if board.is_winner("X"):
        print("\n 'X' wins")
        play_again = raw_input("Play Again ?  [y/N] : ")
        if play_again == "y" or play_again == "Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break
    if board.is_tie():
        print("\n 'Its a Tie")
        play_again = raw_input("Play Again ?  [y/N] : ")
        if play_again == "y" or play_again == "Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break

    # Get O input
    board.ai_move("O")
    # o_choice = int(input("\n Player 'O', Choose from 1 - 9 >>> "))

    # Update Board
    # board.update_cell(o_choice, "O")

    refresh_screen()
    # Check for X wins
    if board.is_winner("O"):
        print("\n 'O' wins")
        play_again = raw_input("Play Again ?  [y/N] : ")
        if play_again == "y" or play_again == "Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break
    if board.is_tie():
        print("\n 'Its a Tie")
        play_again = raw_input("Play Again ?  [y/N] : ")
        if play_again == "y" or play_again == "Y":
            board.reset()
            refresh_screen()
            continue
        else:
            break

