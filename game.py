# import pygame
# import random

# pygame.font.init()

# # GLOBALS VARS
# screen_width = 800
# screen_height = 700
# play_width = 300  # meaning 300 // 10 = 30 width per block
# play_height = 600  # meaning 600 // 20 = 20 height per block
# block_size = 30

# top_left_x = (s_width - play_width) // 2
# top_left_y = s_height - play_height

# # piece arrays
# S = [[[0, 0, 0], 
#       [0, 1, 1], 
#       [1, 1, 0]],
#      [[1, 0, 0], 
#       [1, 1, 0], 
#       [0, 1, 0]],
#      [[0, 1, 1], 
#       [1, 1, 0],
#       [0, 0, 0]],
#      [[0, 1, 0], 
#       [0, 1, 1], 
#       [0, 0, 1]]] 

# Z = [[[0, 0, 0], 
#       [1, 1, 0], 
#       [0, 1, 1]],
#      [[0, 1, 0], 
#       [1, 1, 0], 
#       [1, 0, 0]],
#      [[1, 1, 0], 
#       [0, 1, 1],
#       [0, 0, 0]],
#      [[0, 0, 1], 
#       [0, 1, 1], 
#       [0, 1, 0]]] 
 
# I = [[[0, 0, 0, 0], 
#       [1, 1, 1, 1], 
#       [0, 0, 0, 0], 
#       [0, 0, 0, 0]],
#      [[0, 0, 1, 0], 
#       [0, 0, 1, 0], 
#       [0, 0, 1, 0], 
#       [0, 0, 1, 0]],
#      [[0, 0, 0, 0], 
#       [0, 0, 0, 0], 
#       [1, 1, 1, 1], 
#       [0, 0, 0, 0]],
#      [[0, 1, 0, 0], 
#       [0, 1, 0, 0], 
#       [0, 1, 0, 0], 
#       [0, 1, 0, 0]]] 
 
# O = [[1, 1],
#      [1, 1]]
 
# J = [[[1, 0, 0], 
#       [1, 1, 1], 
#       [0, 0, 0]],
#      [[0, 1, 1], 
#       [0, 1, 0], 
#       [0, 1, 0]],
#      [[0, 0, 0], 
#       [1, 1, 1], 
#       [0, 0, 1]],
#      [[0, 1, 0], 
#       [0, 1, 0], 
#       [1, 1, 0]]]  
 
# L = [[[0, 0, 1], 
#       [1, 1, 1], 
#       [0, 0, 0]],
#      [[0, 1, 0], 
#       [0, 1, 0], 
#       [0, 1, 1]],
#      [[0, 0, 0], 
#       [1, 1, 1], 
#       [1, 0, 0]],
#      [[1, 1, 0], 
#       [0, 1, 0], 
#       [0, 1, 0]]]
 
# T = [[[0, 1, 0], 
#       [1, 1, 1], 
#       [0, 0, 0]],
#      [[0, 1, 0], 
#       [0, 1, 1], 
#       [0, 1, 0]],
#      [[0, 0, 0], 
#       [1, 1, 1], 
#       [0, 1, 0]],
#      [[0, 1, 0], 
#       [1, 1, 0], 
#       [0, 1, 0]]]
 
# shapes = [S, Z, I, O, J, L, T]
# shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]



# board
#     game should be centered
#     a queue

# pieces
#     collision detection
#     piece falls over time
#     freezes when it collides


import pygame
import random

colors = [
    (0, 0, 0),
    (68,172,228), 
    (237,86,89), 
    (86,190,78), 
    (17,101,181), 
    (243,154,39), 
    (123,67,167), 
    (244,212,60)]

#  0  1  2  3 
#  4  5  6  7 
#  8  9 10 11
# 12 13 14 15

queue = [0, 1, 2, 3, 4, 5, 6]
random.shuffle(queue)
hold = []

class Figure:
    
    x = 0
    y = 0
    
    figures = [
        [[4, 5, 6, 7], [1, 5, 9, 13], [8, 9, 10, 11], [2, 6, 10, 14]],
        [[4, 5, 9, 10], [5, 8, 9, 12], [8, 9, 13, 14], [6, 10, 9, 13]],
        [[6, 7, 9, 10], [5, 9, 10, 14], [10, 11, 13, 14], [6, 10, 11, 15]],
        [[0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10], [1, 2, 5, 9]],
        [[2, 4, 5, 6], [0, 1, 5, 9], [4, 5, 6, 8], [1, 5, 9, 10]],
        [[1, 4, 5, 6], [1, 5, 4, 9], [4, 5, 6, 9], [1, 6, 5, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        global queue
        self.x = x
        self.y = y
        if len(queue) == 2:
            newqueue = [0, 1, 2, 3, 4, 5, 6]
            random.shuffle(queue)
            queue += newqueue 
            for i in queue:
                print(i)

        val = random.randint(0, len(self.figures) - 1)
        val = queue[0]
        del queue[0]

        self.type = val
        self.color = val + 1
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
    
    def rotate_180(self):
        self.rotation = (self.rotation + 2) % len(self.figures[self.type])

    def rotate_counter(self):
        self.rotation = (self.rotation - 1) % len(self.figures[self.type])




class Tetris:
    level = 2
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self):
        self.figure = Figure(3, 0)
    
    

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self):
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

    def rotate_180(self):
        old_rotation = self.figure.rotation
        self.figure.rotate_180()
        if self.intersects():
            self.figure.rotation = old_rotation

    def rotate_counter(self):
        old_rotation = self.figure.rotation
        self.figure.rotate_counter()
        if self.intersects():
            self.figure.rotation = old_rotation




# Initialize the game engine
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()
fps = 25
game = Tetris(20, 10)
counter = 0

pressing_down = False

while not done:
    if game.figure is None:
        game.new_figure()
    counter += 1
    if counter > 100000:
        counter = 0

    if counter % (fps // game.level // 2) == 0 or pressing_down:
        if game.state == "start":
            game.go_down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_q:
                game.rotate()
            if event.key == pygame.K_w:
                game.rotate_180()
            if event.key == pygame.K_e:
                game.rotate_counter()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
            if event.key == pygame.K_SPACE:
                game.go_space()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)

    if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

    screen.fill((52,60,68))

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                pygame.draw.rect(screen, colors[game.field[i][j]],
                                 [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color],
                                     [game.x + game.zoom * (j + game.figure.x) + 1,
                                      game.y + game.zoom * (i + game.figure.y) + 1,
                                      game.zoom - 2, game.zoom - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)
    font1 = pygame.font.SysFont('Calibri', 20, True, False)
    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font1.render("Game Over", True, (255, 125, 0))
    text_game_over1 = font1.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == "gameover":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()

