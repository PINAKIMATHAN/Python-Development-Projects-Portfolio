import tkinter as tk
import random
import time

# Constants
WIDTH = 600
HEIGHT = 400
DELAY = 25  # milliseconds
DIFFICULTY_LEVELS = {"Easy": 0.2, "Medium": 0.1, "Hard": 0.05}
SNAKE_SIZE = 20

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.score = 0
        self.speed = 0.1  # Initial speed

        self.score_label = tk.Label(master, text="Score: 0", font=('Helvetica', 12))
        self.score_label.pack()

        self.level_var = tk.StringVar(master)
        self.level_var.set("Medium")
        self.level_menu = tk.OptionMenu(master, self.level_var, *DIFFICULTY_LEVELS.keys())
        self.level_menu.pack()

        self.master.bind('<Key>', self.change_direction)
        self.run_game()

    def create_food(self):
        x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        return x, y

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='green', tag="snake")

    def draw_food(self):
        x, y = self.food
        self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill='red', tag="food")

    def check_collision(self):
        head = self.snake[0]
        if (head in self.snake[1:] or
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT):
            return True
        return False

    def check_food(self):
        head = self.snake[0]
        if head == self.food:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.snake.append(self.snake[-1])  # Grow snake
            self.food = self.create_food()
            self.speed = DIFFICULTY_LEVELS[self.level_var.get()]

    def change_direction(self, event):
        key = event.keysym
        if key in ['Up', 'Down', 'Left', 'Right']:
            if (key == 'Up' and self.direction != 'Down' or
                key == 'Down' and self.direction != 'Up' or
                key == 'Left' and self.direction != 'Right' or
                key == 'Right' and self.direction != 'Left'):
                self.direction = key

    def move_snake(self):
        x, y = self.snake[0]
        if self.direction == 'Up':
            y -= SNAKE_SIZE
        elif self.direction == 'Down':
            y += SNAKE_SIZE
        elif self.direction == 'Left':
            x -= SNAKE_SIZE
        elif self.direction == 'Right':
            x += SNAKE_SIZE
        self.snake = [(x, y)] + self.snake[:-1]

    def run_game(self):
        if self.check_collision():
            self.game_over()
            return

        self.move_snake()
        self.check_food()
        self.draw_snake()
        self.draw_food()

        self.master.after(int(DELAY / self.speed), self.run_game)

    def game_over(self):
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2, text=f"Game Over! Score: {self.score}", fill="white",
                                font=('Helvetica', 24))
        self.master.unbind('<Key>')  # Unbind key events

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
