import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None]*3 for _ in range(3)]
        self.create_widgets()
        self.player_X_score = 0
        self.player_O_score = 0

    def create_widgets(self):
        self.scoreboard = tk.Label(self.master, text="Scoreboard: X - 0, O - 0", font=('Helvetica', 12))
        self.scoreboard.grid(row=0, column=0, columnspan=3)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text='', font=('Helvetica', 20), width=5, height=2,
                                                command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)

        self.reset_button = tk.Button(self.master, text="Reset", font=('Helvetica', 12), command=self.reset)
        self.reset_button.grid(row=4, column=1, columnspan=3, pady=10)

    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state='disabled', disabledforeground='black')

            if self.check_winner():
                self.update_scoreboard()
                messagebox.showinfo("Congratulations!", f"Player {self.current_player} wins!")
                self.reset()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset()
            else:
                self.switch_player()

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal')
                self.board[i][j] = ' '
        self.current_player = 'X'

    def update_scoreboard(self):
        if self.current_player == 'X':
            self.player_X_score += 1
        else:
            self.player_O_score += 1
        self.scoreboard.config(text=f"Scoreboard: X - {self.player_X_score}, O - {self.player_O_score}")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
