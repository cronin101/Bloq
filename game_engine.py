import math
from pyglet.graphics import *
from pyglet.gl import *
from itertools import chain


class GameEngine(object):
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.batch = Batch()

    def orient(self):
        loc = self.game.loc

        width, height = self.window.get_size()
        glEnable(GL_DEPTH_TEST)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, width / float(height), 0.1, 60.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        x, y = loc.rotation
        glRotatef(x, 0, 1, 0)
        glRotatef(-y, math.cos(math.radians(x)), 0, math.sin(math.radians(x)))

        x, y, z = loc.position
        glTranslatef(-x, -(y + 1), -z)

    def draw(self):
        self.window.clear()
        glColor3d(1, 1, 1)
        '''Draw Axes'''
        length = 24.0
        wall_y = list(chain.from_iterable(
            [-length, float(y), 0.0, length, float(y), 0.0] for y in xrange(int(length))))

        wall_x = list(chain.from_iterable(
            [float(x - length), 0, 0.0, float(x - length), length, 0.0] for x in xrange(2 * int(length))))

        floor_y = list(chain.from_iterable(
            [float(x - length), 0.0, 0.0, float(x - length), 0.0, length] for x in xrange(2 * int(length))))

        floor_x = list(chain.from_iterable(
            [length, 0.0, float(x), -length, 0.0, float(x)] for x in xrange(int(length))))

        colors = [  1.0,0.0,0.0, 1.0,0.0,0.0, \
                    0.0,1.0,0.0, 0.0,1.0,0.0, \
                    0.0,0.0,1.0, 0.0,0.0,1.0  ]

        vset = wall_y + wall_x  + floor_y + floor_x

        self.batch.add(len(vset) // 3, GL_LINES, None,
            ('v3f/static', vset))
            #('c3f/static', (colors[0] * 10) + (colors[1] * 10) + colors[2]))

        self.batch.draw()



