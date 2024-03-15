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

space = 9
def square(width: int, height: int) -> None:
    nodes = []
    for y in range(height):
        nodes.append([])
        for x in range(width):
            nodes[-1].append(Node((200 + x * space, 200 + y * space)))
            if y > 0: Stick(nodes[y][x], nodes[y - 1][x], space)
            if x > 0: Stick(nodes[y][x], nodes[y][x - 1], space)
            if x > 0 and y > 0: Stick(nodes[y][x], nodes[y - 1][x - 1], space * sqrt(2))
            if x < width - 1 and y > 0: Stick(nodes[y][x], nodes[y - 1][x + 1], space * sqrt(2))

square(25, 10)

# n1 = Node((250, 250))
# n2 = Node((240, 260))
# n3 = Node((260, 260))
# n4 = Node((230, 270))
# n5 = Node((250, 270))
# n6 = Node((270, 270))
# n7 = Node((240, 280))
# n8 = Node((260, 280))
# n9 = Node((250, 290))
# Stick(n1, n2, 20)
# Stick(n2, n3, 20)
# Stick(n1, n3, 20)
# Stick(n2, n4, 20)
# Stick(n2, n5, 20)
# Stick(n4, n5, 20)
# Stick(n3, n5, 20)
# Stick(n3, n6, 20)
# Stick(n5, n6, 20)
# Stick(n4, n7, 20)
# Stick(n5, n7, 20)
# Stick(n5, n8, 20)
# Stick(n6, n8, 20)
# Stick(n7, n8, 20)
# Stick(n7, n9, 20)
# Stick(n8, n9, 20)

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