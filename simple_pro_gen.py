import random
import pygame

pygame.init()

x, y = 10, 10
width, height = 40, 40
steps = 600
counter = 0

level = [['x' for _ in range(width)] for _ in range(height)]

while steps > 0:
    if level[y][x] == 'x':
        level[y][x] = ' '
        steps -= 1
        counter += 1

    dir = random.randint(1, 4)

    if dir == 1 and y > 2:
        y -= 1
    if dir == 2 and y < height - 3:
        y += 1
    if dir == 3 and x > 2:
        x -= 1
    if dir == 4 and x < width - 3:
        x += 1

for row in level:
    print(" ".join(row))

class Player:
    def __init__(self, screen, offset):
        self.screen = screen
        self.offset = offset

        self.x, self.y = 1000, 1000
        self.rect = pygame.Rect(self.x - self.offset[0], self.y - self.offset[1], 40, 40)

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_s]:
            self.y += 5
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_d]:
            self.x += 5

        self.rect.topleft = (self.x - self.offset[0], self.y - self.offset[1])

    def update(self):
        self.draw()
        self.movement()

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((700, 700))
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()
        self.offset = [0, 0]
        self.pl = Player(self.screen, self.offset)
        self.rects = []

    def draw_map(self):
        for y, a in enumerate(level):
            for x, b in enumerate(a):
                if b == 'x':
                    self.rects.append([x, y])

    def update(self):
        self.draw_map()
        run = True
        while run:
            self.screen.fill((0, 0, 0))
            self.events = pygame.event.get()

            self.offset[0] += (self.pl.x - self.offset[0] - 330)/10
            self.offset[1] += (self.pl.y - self.offset[1] - 330)/10

            for event in self.events:
                if event.type == pygame.QUIT:
                    run = False

            for rect in self.rects[:]:
                pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(rect[0] * 100 - self.offset[0], rect[1] * 100 - self.offset[1], 100, 100))
            self.pl.update()

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

Game().update()