from pyglet.window import key


class PlayerController(object):
    def __init__(self, game):
        self.game = game

    def handle_key_input(self, symbol, modifiers):
        if symbol   == 119: self.game.walk(forward=True)  # W
        elif symbol == 115: self.game.walk(forward=False) # S
        elif symbol == 97: self.game.strafe(right=False)  # A
        elif symbol == 100: self.game.strafe(right=True)  # D
        elif symbol == 32: self.game.jump()               # Space
        else:
            print(symbol)

    def handle_mouse_movement(self, dx, dy):
        scale = 0.1
        self.game.rotate(scale * dx, scale * dy)


