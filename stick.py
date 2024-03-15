from vector import Vector2
from node import Node
from math import *
import pygame

class Stick:
    instances = []

    def __init__(self, node1: Node, node2: Node, length: int) -> None:
        self.instances.append(self)
        self.node1 = node1
        self.node2 = node2
        self.length = length

        node1.connections += 1
        node2.connections += 1

    def update(self, dt: float) -> None:
        dist = self.node1.pos.distance_to(self.node2.pos)
        perc = (1 - self.length / dist) * 0.5
        disp = (self.node2.pos - self.node1.pos) * perc
        self.node1.pos += disp * 0.4
        self.node2.pos -= disp * 0.4

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.line(screen, (255, 255, 255), self.node1.pos, self.node2.pos)