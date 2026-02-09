import tkinter as tk
import random
import time

# Constants
DELAY = {'easy': 150, 'medium': 100, 'hard': 50}
GRID_SIZE = 20
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SNAKE_COLOR = 'green'
FOOD_COLOR = 'red'
SCORE_FONT = ('Helvetica', 14)

class SnakeGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Snake Game')
        self.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, bg='black', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.score = 0
        self.score_label = tk.Label(self, text=f'Score: {self.score}', font=SCORE_FONT, fg='white', bg='black')
        self.score_label.pack()

        self.level_var = tk.StringVar()
        self.level_var.set('easy')
        level_frame = tk.Frame(self)
        level_frame.pack()
        for level in ['easy', 'medium', 'hard']:
            level_button = tk.Radiobutton(level_frame, text=level.capitalize(), variable=self.level_var, value=level)
            level_button.pack(side='left')

        self.reset()

    def reset(self):
        self.direction = 'Right'
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.generate_food()
        self.score = 0
        self.update_score()
        self.delay = DELAY[self.level_var.get()]
        self.game_over = False
        self.bind_keys()
        self.update()

    def bind_keys(self):
        self.bind('<Up>', lambda event: self.change_direction('Up'))
        self.bind('<Down>', lambda event: self.change_direction('Down'))
        self.bind('<Left>', lambda event: self.change_direction('Left'))
        self.bind('<Right>', lambda event: self.change_direction('Right'))

    def change_direction(self, direction):
        if direction == 'Up' and self.direction != 'Down':
            self.direction = direction
        elif direction == 'Down' and self.direction != 'Up':
            self.direction = direction
        elif direction == 'Left' and self.direction != 'Right':
            self.direction = direction
        elif direction == 'Right' and self.direction != 'Left':
            self.direction = direction

    def generate_food(self):
        while True:
            x = random.randint(0, (CANVAS_WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            y = random.randint(0, (CANVAS_HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
            if (x, y) not in self.snake:
                return x, y

    def update_score(self):
        self.score_label.config(text=f'Score: {self.score}')

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'Up':
            head_y -= GRID_SIZE
        elif self.direction == 'Down':
            head_y += GRID_SIZE
        elif self.direction == 'Left':
            head_x -= GRID_SIZE
        elif self.direction == 'Right':
            head_x += GRID_SIZE

        self.snake.insert(0, (head_x, head_y))

        if head_x == self.food[0] and head_y == self.food[1]:
            self.score += 1
            self.update_score()
            self.food = self.generate_food()
        else:
            self.snake.pop()

        self.check_collision()

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= CANVAS_WIDTH or head_y < 0 or head_y >= CANVAS_HEIGHT or (head_x, head_y) in self.snake[1:]:
            self.game_over = True

    def draw(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + GRID_SIZE, self.food[1] + GRID_SIZE, fill=FOOD_COLOR)

        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR)

    def update(self):
        if not self.game_over:
            self.move()
            self.draw()
            self.after(self.delay, self.update)
        else:
            self.game_over_screen()

    def game_over_screen(self):
        self.canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text=f'Game Over\nScore: {self.score}', font=SCORE_FONT, fill='white')
        self.after(3000, self.reset)

if __name__ == "__main__":
    game = SnakeGame()
    game.mainloop()
