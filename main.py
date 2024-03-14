from pygame.locals import *
from vector import VEC
from node import Node
import pygame

WIDTH, HEIGHT = 400, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

n1 = Node((100, 100), root=True)
n2 = Node((100, 100), n1)
n3 = Node((100, 100), n2, n1)
n4 = Node((100, 100), n2)
n5 = Node((100, 100), n2, n3, n4)
n6 = Node((100, 100), n3, n5)
n7 = Node((100, 100), n4, n5)
n8 = Node((100, 100), n5, n6, n7)
n9 = Node((100, 100), n7, n8)

# grid = []
# for y in range(7):
#     grid.append([])
#     for x in range(7):
#         grid[y].append(Node((50 + x * 10, 50 + y * 10)))
#         if y > 0: grid[y][x].add_connection(grid[y - 1][x])
#         if x > 0: grid[y][x].add_connection(grid[y][x - 1])
#         if x > 0 and y > 0: grid[y][x].add_connection(grid[y - 1][x - 1])
# grid[0][0].root = True

running = True
while running:
    dt = clock.tick(144) * 0.05

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    for node in Node.instances:
        node.update(dt)
        node.draw(screen)

    pygame.display.flip()

pygame.quit()