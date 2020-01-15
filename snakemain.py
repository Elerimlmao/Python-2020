import pygame
import random
import math
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        self.color = color
        sef.head = cube(pos)
        self.body.append(self.head)

        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for even in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            keys = pygame.key.get_pressed()

            for key in keys:
                ifkeys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass

def drawGrid(w, rows, surface):
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    surface.fill((0, 0, 0))
    drawGrid(surface)
    pygame.display.update()

def randomSnack(rows, iteam):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows, s
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width, height))
    s = snake((255, 0, 0), (10, 10))

    clock = pygame.time.Clock()
    flag = True
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)

main()
    
