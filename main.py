from pygame.locals import *
from stick import Stick
from vector import VEC
from node import Node
import pygame

WIDTH, HEIGHT = 800, 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

space = 9
def rhombus(size: int):
    nodes = []
    for i in range(1, size + 1):
        nodes.append([])
        for j in range(i):
            nodes[-1].append(Node((200 + j * space - i * space * 0.5, 200 + i * space)))
    for i in range(1, size):
        nodes.append([])
        for j in range(size - i):
            nodes[-1].append(Node((200 + j * space + i * space * 0.5 - size * space * 0.5, 200 + size * space + i * space)))
    for y, row in enumerate(nodes):
        for x, node in enumerate(row):
            try:
                if y > 0:
                    Stick(node, nodes[y - 1][x], space)
            except IndexError:
                pass
            try:
                if x > 0:
                    Stick(node, nodes[y][x - 1], space)
            except IndexError:
                pass
            if y < size:
                try:
                    if x > 0:
                        Stick(node, nodes[y - 1][x - 1], space)
                except IndexError:
                    pass
            else:
                try:
                    Stick(node, nodes[y - 1][x + 1], space)
                except IndexError:
                    pass

rhombus(25)

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