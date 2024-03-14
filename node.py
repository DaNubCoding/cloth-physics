from typing import Self
from vector import VEC
from random import *
from math import *
import pygame

class Node:
    instances = []

    def __init__(self, pos: VEC, *connections: tuple[Self], root: bool = False) -> None:
        self.instances.append(self)
        self.root = root
        self.pos = VEC(pos)
        self.vel = VEC(uniform(-0.01, 0.01), uniform(-0.01, 0.01))
        self.connections = list(connections)
        for node in connections:
            node.add_connection(self)

    def update(self, dt: float) -> None:
        if self.root:
            if pygame.mouse.get_pressed()[0]:
                self.pos += (VEC(pygame.mouse.get_pos()) - self.pos) * 0.05
            return

        self.vel.y += 0.5 * dt
        self.vel *= 0.9 ** dt
        self.pos += self.vel * dt

        for node in self.connections:
            self.handle(node)

    def handle(self, other: Self) -> None:
        self.vel += (other.pos + (self.pos - other.pos).normalize() * 20 - self.pos) * 0.03

    def add_connection(self, node: Self) -> None:
        self.connections.append(node)

    def draw(self, screen: pygame.Surface) -> None:
        for node in self.connections:
            pygame.draw.line(screen, (255, 255, 255), self.pos, node.pos)
        pygame.draw.circle(screen, (255, 0, 0), self.pos, 3)