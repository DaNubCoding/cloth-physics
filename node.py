from timer import LoopTimer
from typing import Self
from vector import VEC
from random import *
from math import *
import pygame

class Node:
    instances = []
    wind = VEC(0.3, 0)
    wind_timer = LoopTimer(lambda: uniform(0.05, 0.2))

    @staticmethod
    def update_wind() -> None:
        if Node.wind_timer.ended:
            Node.wind = VEC(uniform(0.1, 0.5), uniform(-0.15, 0.15)) * 0.2 * 0

    def __init__(self, pos: VEC) -> None:
        self.instances.append(self)
        self.pos = VEC(pos)
        self.prev_pos = self.pos + VEC(uniform(-0.01, 0.01), uniform(-0.01, 0.01))
        self.connections = 0
        self.picked = False

    def update(self, dt: float) -> None:
        vel = self.pos - self.prev_pos
        self.prev_pos = self.pos.copy()

        if self.picked:
            self.pos += (VEC(pygame.mouse.get_pos()) - self.pos) * 0.6
            return

        self.pos += vel * 0.995 # basically air resistance
        self.pos.y += 0.1 # gravity
        wind_multiplier = self.connections * 0.5
        self.pos += self.wind * wind_multiplier

        self.handle_edge()

    def handle_edge(self) -> None:
        if self.pos.x < 0:
            self.pos.x = 0 - (self.pos.x - 0)
            self.prev_pos.x = 0 - (self.prev_pos.x - 0)
            self.prev_pos.x -= (self.prev_pos.x - self.pos.x) * 1 # Bounciness factor (1 is 100% energy absorption)
            self.prev_pos.y -= (self.prev_pos.y - self.pos.y) * 0.3 # Wall & ground friction factor
        elif self.pos.x > 800:
            self.pos.x = 800 - (self.pos.x - 800)
            self.prev_pos.x = 800 - (self.prev_pos.x - 800)
            self.prev_pos.x -= (self.prev_pos.x - self.pos.x) * 1
            self.prev_pos.y -= (self.prev_pos.y - self.pos.y) * 0.3
        if self.pos.y < 0:
            self.pos.y = 0 - (self.pos.y - 0)
            self.prev_pos.y = 0 - (self.prev_pos.y - 0)
            self.prev_pos.y -= (self.prev_pos.y - self.pos.y) * 1
            self.prev_pos.x -= (self.prev_pos.x - self.pos.x) * 0.3
        elif self.pos.y > 800:
            self.pos.y = 800 - (self.pos.y - 800)
            self.prev_pos.y = 800 - (self.prev_pos.y - 800)
            self.prev_pos.y -= (self.prev_pos.y - self.pos.y) * 1
            self.prev_pos.x -= (self.prev_pos.x - self.pos.x) * 0.3

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 2)