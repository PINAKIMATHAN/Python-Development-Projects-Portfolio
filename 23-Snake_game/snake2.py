import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg='black')
        self.canvas.pack()
        
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.create_food()
        self.direction = "Left"
        self.score = 0
        self.bonus_points = 0
        self.score_label = tk.Label(self.master, text="Score: {}".format(self.score), font=('Helvetica', 12))
        self.score_label.pack()
        
        self.speed = 100
        self.game_over = False
        
        self.draw_snake()
        self.draw_food()
        
        self.master.bind("<Key>", self.change_direction)
        self.move_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill='yellow', tags="snake")

    def draw_food(self):
        self.canvas.delete("food")
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill='red', tags="food")
        
    def create_food(self):
        return (random.randint(0, 39)*10, random.randint(0, 39)*10)
    
    def move_snake(self):
        if not self.game_over:
            head = self.snake[0]
            if self.direction == "Up":
                new_head = (head[0], head[1] - 10)
            elif self.direction == "Down":
                new_head = (head[0], head[1] + 10)
            elif self.direction == "Left":
                new_head = (head[0] - 10, head[1])
            elif self.direction == "Right":
                new_head = (head[0] + 10, head[1])

            if new_head in self.snake or new_head[0] < 0 or new_head[0] >= 400 or new_head[1] < 0 or new_head[1] >= 400:
                self.game_over = True
                self.canvas.create_text(200, 200, text="Game Over!", fill='white', font=('Helvetica', 24))
            else:
                self.snake = [new_head] + self.snake
                if new_head == self.food:
                    self.score += 10 + self.bonus_points
                    self.score_label.config(text="Score: {}".format(self.score))
                    self.food = self.create_food()
                    self.bonus_points = 0
                else:
                    self.snake.pop()
                    if self.bonus_points > 0:
                        self.bonus_points -= 1
                self.draw_snake()
                self.draw_food()
                self.master.after(self.speed, self.move_snake)
    
    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (event.keysym == "Up" and self.direction != "Down") or \
               (event.keysym == "Down" and self.direction != "Up") or \
               (event.keysym == "Left" and self.direction != "Right") or \
               (event.keysym == "Right" and self.direction != "Left"):
                self.direction = event.keysym

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
