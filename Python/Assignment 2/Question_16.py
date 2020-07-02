"""Imagine you are creating a Super Mario game. You need to define
a class to represent Mario. What would it look like? If you aren't
familiar with SuperMario, use your own favorite video or board game
to model a player."""


class Mario:
    def __init__(self):
        self._lives = 3
        self._speed = 10
        self._jumpheight = 5
        self._width = 32
        self._height = 64
        self._sprite = "/path-to-sprite.png"

    def draw(self, screen):
        return

    def update(self, delta_time):
        return

    def move(self, direction): n
    return

    def jump(self):
        return

    def collides(self, other):
        return
