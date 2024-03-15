from pygame.locals import *
from stick import Stick
from vector import VEC
from node import Node
from math import *
import pygame

WIDTH, HEIGHT = 800, 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

def square(width: int, height: int, space: int) -> None:
    nodes = []
    for y in range(height):
        nodes.append([])
        for x in range(width):
            nodes[-1].append(Node((200 + x * space, 200 + y * space)))
            if y > 0: Stick(nodes[y][x], nodes[y - 1][x], space)
            if x > 0: Stick(nodes[y][x], nodes[y][x - 1], space)
            if x > 0 and y > 0: Stick(nodes[y][x], nodes[y - 1][x - 1], space * sqrt(2))
            if x < width - 1 and y > 0: Stick(nodes[y][x], nodes[y - 1][x + 1], space * sqrt(2))

square(25, 10, 12)

running = True
while running:
    dt = clock.tick(144) * 0.05
    pygame.display.set_caption(f"{clock.get_fps():.1f}")

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            min_dist = float("inf")
            min_node = None
            mpos = VEC(pygame.mouse.get_pos())
            for node in Node.instances:
                if (dist := node.pos.distance_to(mpos)) < min_dist:
                    min_dist = dist
                    min_node = node
            min_node.picked = True
        if event.type == MOUSEBUTTONUP:
            for node in Node.instances:
                node.picked = False

    screen.fill((0, 0, 0))

    Node.update_wind()

    for node in Node.instances:
        node.update(dt)

    for stick in Stick.instances:
        stick.update(dt)

    for node in Node.instances:
        node.draw(screen)

    for stick in Stick.instances:
        stick.draw(screen)

    pygame.display.flip()

pygame.quit()