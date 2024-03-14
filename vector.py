from multimethod import multimeta as _multimeta
from pygame.math import Vector2
from typing import Self

class VEC(Vector2, metaclass=_multimeta):
    def normalize(self) -> Self:
        try:
            return super().normalize()
        except ValueError:
            return VEC(0, 0)

    def normalize_ip(self) -> None:
        try:
            return super().normalize_ip()
        except ValueError:
            pass

    def clamp_magnitude(self, max_length: float) -> Self:
        try:
            return super().clamp_magnitude(max_length)
        except ValueError:
            return VEC(0, 0)

    def clamp_magnitude(self, min_length: float, max_length: float) -> Self:
        try:
            return super().clamp_magnitude(min_length, max_length)
        except ValueError:
            return VEC(0, 0)

    def clamp_magnitude_ip(self, max_length: float) -> None:
        try:
            return super().clamp_magnitude_ip(max_length)
        except ValueError:
            pass

    def clamp_magnitude_ip(self, min_length: float, max_length: float) -> None:
        try:
            return super().clamp_magnitude_ip(min_length, max_length)
        except ValueError:
            pass

    def __hash__(self) -> int:
        return tuple(self).__hash__()