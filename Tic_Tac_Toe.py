import time
import random
ttt="""
⟦T⟧⟦i⟧⟦c⟧ ⟦T⟧⟦a⟧⟦c⟧ ⟦T⟧⟦o⟧⟦e⟧
"""
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.player_names = {'X': 'Player X', 'O': 'Player O'}

    def display_board(self):
        print(f"\n\n --------------- {ttt} ----------------\n\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def get_player_move(self):
        while True:
            try:
                position = int(input(f"\n{self.player_names[self.current_player]}'s turn. Choose a position (1-9): "))
                if 1 <= position <= 9 and self.board[position - 1] == ' ':
                    return position
                else:
                    print("Invalid move. Please choose a valid position.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def make_move(self, position):
        self.board[position - 1] = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ' or \
               self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != ' ':
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ' or \
           self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        return False

    def is_tie(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.display_board()
            if self.player_names[self.current_player] == 'Computer':
                position = self.get_computer_move()
            else:
                position = self.get_player_move()
            self.make_move(position)

            if self.check_winner():
                self.display_board()
                print(f"\nPlayer {self.player_names[self.current_player]} wins!\n")
                time.sleep(2)  # Add a 2-second delay
                
                break
            elif self.is_tie():
                self.display_board()
                print("\nThe game is a tie!\n")
                time.sleep(2)  # Add a 2-second delay
                

                break
            

            self.switch_player()
        
        play_again = input("\n\nDo you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            self.reset_game()
            self.play()
        else:
            print("\nThank you for playing Tic Tac Toe!")

    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def get_game_mode(self):
        while True:
            mode = input("\nChoose game mode: (1) Play with a friend or (2) Play with computer: ").lower()
            if mode == '1':
                return 'friend'
            elif mode == '2':
                return 'computer'
            else:
                print("Invalid choice. Please enter '1' or '2'.")

    def setup_players(self, mode):
        if mode == 'friend':
            self.player_names['X'] = input("\nEnter name for Player X: ")
            self.player_names['O'] = input("Enter name for Player O: ")
            while True:
                choice = input(f"{self.player_names['X']}, do you want to be X or O? ").upper()
                if choice in ['X', 'O']:
                    if choice == 'O':
                        self.current_player = 'O'
                        self.player_names['X'], self.player_names['O'] = self.player_names['O'], self.player_names['X']
                    break
                else:
                    print("Invalid choice. Please enter 'X' or 'O'.")
            print(f"\n{self.player_names['X']} will be X and {self.player_names['O']} will be O.")
        elif mode == 'computer':
            self.player_names['X'] = input("\nEnter your name: ")
            self.player_names['O'] = 'Computer'
            while True:
                choice = input(f"{self.player_names['X']}, do you want to be X or O? ").upper()
                if choice in ['X', 'O']:
                    if choice == 'O':
                        self.current_player = 'O'
                        self.player_names['X'], self.player_names['O'] = self.player_names['O'], self.player_names['X']
                    break
                else:
                    print("Invalid choice. Please enter 'X' or 'O'.")
            print(f"\n{self.player_names['X']} will be X and {self.player_names['O']} will be O.")
        elif mode == 'computer':
            self.player_names['X'] = input("\nEnter your name: ")
            self.player_names['O'] = 'Computer'
            while True:
                choice = input(f"{self.player_names['X']}, do you want to be X or O? ").upper()
                if choice in ['X', 'O']:
                    if choice == 'O':
                        self.current_player = 'O'
                        self.player_names['X'], self.player_names['O'] = self.player_names['O'], self.player_names['X']
                    break
                else:
                    print("Invalid choice. Please enter 'X' or 'O'.")
            print(f"\n{self.player_names['X']} will be X and {self.player_names['O']} will be O.")
        else:
            print("Invalid game mode. Please choose 'friend' or 'computer'.")

    def get_computer_move(self):
        print(f"\n{self.player_names[self.current_player]}'s turn.")
        time.sleep(1) # Simulate thinking time
        # Check for a winning move
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.current_player
                if self.check_winner():
                    self.board[i] = ' '
                    return i + 1
                self.board[i] = ' '

        # Check if the opponent can win and block them
        opponent = 'O' if self.current_player == 'X' else 'X'
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = opponent
                if self.check_winner():
                    self.board[i] = ' '
                    return i + 1
                self.board[i] = ' '

        # Try to take the center
        if self.board[4] == ' ':
            return 5

        # Try to take a corner
        corners = [0, 2, 6, 8]
        available_corners = [i for i in corners if self.board[i] == ' ']
        if available_corners:
            return random.choice(available_corners) + 1

        # Take any available side
        sides = [1, 3, 5, 7]
        available_sides = [i for i in sides if self.board[i] == ' ']
        if available_sides:
            return random.choice(available_sides) + 1

        return -1 # Should not happen in a tie-checked game
        
        


if __name__ == "__main__":
    game = TicTacToe()
    game_mode = game.get_game_mode()
    game.setup_players(game_mode)
    game.play()




