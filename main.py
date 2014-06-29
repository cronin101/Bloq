import pyglet as pl
from pyglet.window import key

from game import GameContext
from game_engine import GameEngine
from player_controller import PlayerController


if __name__ == "__main__":
    window = pl.window.Window()#fullscreen=True)
    game = GameContext()
    game.engine = GameEngine(game, window)

    key_handler = key.KeyStateHandler()
    window.push_handlers(key_handler)

    @window.event
    def on_draw():
        if not game.has_started:
            '''Display initial welcoming screen.'''
            window.clear()
            label = pl.text.Label('Welcome to BloqWorld!',
                    x=window.width/2, y=window.height/2,
                    anchor_x='center', anchor_y='center')
            label.draw()

        else:
            game.engine.orient()
            game.engine.draw()

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        if game.has_started:
            game.controller.handle_mouse_movement(dx, dy)

    def tick(dt):
        game.slide()
        for key, state in key_handler.iteritems():
            if state:
                if not game.has_started:
                    game.controller = PlayerController(game)
                    game.start()
                    window.set_exclusive_mouse(True)
                else:
                    game.controller.handle_key_input(key, None)

    pl.clock.schedule_interval(tick, 1/50.0)

    pl.app.run()
