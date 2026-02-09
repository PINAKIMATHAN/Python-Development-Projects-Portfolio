import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tic Tac Toe')
        self.window.configure(bg='#8ca6fa')

        self.frame = tk.Frame(master=self.window)
        self.frame.pack(pady=10)

        self.label = tk.Label(master=self.frame, text="TIC TAC TOE", font=("Arial", 20, 'bold'), bg='#8ca6fa')
        self.label.pack()

        self.frame1 = tk.Frame(master=self.window, borderwidth=2, relief=tk.SUNKEN, bg='#d7fc03')
        self.frame1.pack(padx=10, pady=10)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(master=self.frame1, text='', width=10, height=5, bg='#92f7be',
                                                command=lambda row=i, col=j: self.button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.frame2 = tk.Frame(master=self.window, border=2, relief=tk.SUNKEN, bg='#f2fac3')
        self.frame2.pack()
        
        self.label1 = tk.Label(master=self.frame2, text="Player 1 --> X\nPlayer 2 --> O", width=10, bg='#f2fac3')
        self.label1.grid(row=0, column=0, padx=5)
        
        self.button_restart = tk.Button(master=self.frame2, text="Restart", width=10, height=3, bg='#eac3fa', relief=tk.GROOVE, command=self.restart)
        self.button_restart.grid(row=0, column=1, padx=10, pady=10)
        
        self.label2 = tk.Label(master=self.frame2, text='Player-1 Turn', bg="skyblue", width=10, height=3, relief=tk.SUNKEN)
        self.label2.grid(row=0, column=2, padx=5)

        self.scoreboard_frame = tk.Frame(master=self.window, border=2, relief=tk.SUNKEN, bg='#f2fac3')
        self.scoreboard_frame.pack(pady=10)
        
        self.player1_score = 0
        self.player2_score = 0
        
        self.player1_label = tk.Label(master=self.scoreboard_frame, text="Player 1 Score: ", bg='#f2fac3')
        self.player1_label.grid(row=0, column=0, padx=5, pady=5)
        
        self.player1_score_label = tk.Label(master=self.scoreboard_frame, text=str(self.player1_score), bg='#f2fac3')
        self.player1_score_label.grid(row=0, column=1, padx=5, pady=5)
        
        self.player2_label = tk.Label(master=self.scoreboard_frame, text="Player 2 Score: ", bg='#f2fac3')
        self.player2_label.grid(row=1, column=0, padx=5, pady=5)
        
        self.player2_score_label = tk.Label(master=self.scoreboard_frame, text=str(self.player2_score), bg='#f2fac3')
        self.player2_score_label.grid(row=1, column=1, padx=5, pady=5)

        self.current_player = "X"
        self.moves = 0
        self.game_over = False

    def button_click(self, row, col):
        if not self.game_over and self.buttons[row][col]["text"] == "":
            self.buttons[row][col]["text"] = self.current_player
            self.moves += 1
            if self.check_winner():
                self.update_scoreboard()
                messagebox.showinfo("Congratulations!", f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.moves == 9:
                messagebox.showinfo("Tie!", "The game is a tie!")
                self.game_over = True
            else:
                self.toggle_player()

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label2.config(text=f"Player-{self.current_player} Turn")

    def check_winner(self):
        board = [[self.buttons[i][j]["text"] for j in range(3)] for i in range(3)]
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return True
            if board[0][i] == board[1][i] == board[2][i] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] != "":
            return True
        if board[0][2] == board[1][1] == board[2][0] != "":
            return True
        return False

    def update_scoreboard(self):
        if self.current_player == "X":
            self.player1_score += 1
            self.player1_score_label.config(text=str(self.player1_score))
        else:
            self.player2_score += 1
            self.player2_score_label.config(text=str(self.player2_score))

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"
        self.moves = 0
        self.game_over = False
        self.label2.config(text='Player-1 Turn')

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
