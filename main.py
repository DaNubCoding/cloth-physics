from pygame.locals import *
from vector import VEC
from node import Node
import pygame

WIDTH, HEIGHT = 800, 800

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

n1 = Node((200, 200), root=True)
n2 = Node((200, 200), n1)
n3 = Node((200, 200), n2, n1)
n4 = Node((200, 200), n2)
n5 = Node((200, 200), n2, n3, n4)
n6 = Node((200, 200), n3, n5)
n7 = Node((200, 200), n4, n5)
n8 = Node((200, 200), n5, n6, n7)
n9 = Node((200, 200), n7, n8)

n1 = Node((100, 100), root=True)

n2 = Node((90, 120), n1)
n3 = Node((110, 120), n2, n1)

n4 = Node((80, 140), n2)
n5 = Node((100, 140), n2, n3, n4)
n6 = Node((120, 140), n3, n5)

n7 = Node((70, 160), n4)
n8 = Node((90, 160), n4, n5, n7)
n9 = Node((110, 160), n5, n6, n8)
n10 = Node((130, 160), n6, n9)

n11 = Node((80, 180), n7, n8)
n12 = Node((100, 180), n8, n9, n11)
n13 = Node((120, 180), n9, n10, n12)

n14 = Node((90, 180), n11, n12)
n15 = Node((110, 180), n12, n13, n14)

n16 = Node((100, 200), n14, n15)

# grid = []
# for y in range(7):
#     grid.append([])
#     for x in range(7):
#         grid[y].append(Node((50 + x * 10, 50 + y * 10)))
#         if y > 0: grid[y][x].add_connection(grid[y - 1][x])
#         if x > 0: grid[y][x].add_connection(grid[y][x - 1])
#         if x > 0 and y > 0: grid[y][x].add_connection(grid[y - 1][x - 1])
# grid[0][0].root = True

# grid = []
# for y in range(5):
#     grid.append([])
#     for x in range(5):
#         grid[y].append(Node((100 + 20 * x, 100 + 20 * y), root = y == 0))
#         if y != 0: grid[y][x].add_connection(grid[y - 1][x])
#         if x != 0: grid[y][x].add_connection(grid[y][x - 1])

running = True
while running:
    dt = clock.tick(144) * 0.05
    pygame.display.set_caption(f"{clock.get_fps():.1f}")

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill((0, 0, 0))

    Node.update_wind()

    for node in Node.instances:
        node.update(dt)
        node.draw(screen)

    pygame.display.flip()

pygame.quit()