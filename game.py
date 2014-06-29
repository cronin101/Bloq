import math

class GameContext(object):
    def __init__(self):
        self.has_started = False
        self.loc = lambda: None
        self.loc.rotation = [0, 0]
        self.loc.position = [0, 0, 10]
        self.loc.velocity = [0, 0, 0]

    def start(self):
        self.has_started = True

    def walk(self, forward=True):
        self.slide()
        direction = 1 if forward else -1
        x, y, z = self.loc.position
        dx, dy, dz = self.__directed_walk(direction)
        self.loc.position = [x + dx, y + dy, z + dz]
        self.loc.velocity = [dx, dy, dz]

    def strafe(self, right=True):
        self.slide()
        direction = -1 if right else 1
        x, y, z = self.loc.position
        dz, dy, dx = self.__directed_walk(direction)
        self.loc.position = [x + 2*dx, y + dy, z - 2*dz]
        #self.loc.velocity = [dx, dy, -dz]

    def slide(self):
        x, y, z = self.loc.position
        dx, dy, dz = self.loc.velocity
        self.loc.position = [x + dx, y + dy, z + dz]
        dx = self.__shift_towards_zero(dx, 0.05)
        if abs(dx) <= 0.001:
            dx = 0
        dz = self.__shift_towards_zero(dz, 0.05)
        if abs(dz) <= 0.001:
            dz = 0

        self.loc.velocity = [dx, dy, dz]

    def rotate(self, dx, dy):
        x, y = self.loc.rotation
        #x = min(x + dx, 90)
        #x = max(x, 0)
        y = min(y + dy, 90)
        y = max(y, -90)

        self.loc.rotation = [x + dx, y]

    def __directed_walk(self, direction):
        scale = 0.10
        xd, yd = self.loc.rotation
        xr, yr = math.radians(xd), math.radians(yd)
        return scale *  math.sin(xr) * direction, 0, scale * (- math.cos(xr)) * direction


    def __shift_towards_zero(self, number, delta):
        return math.copysign(1, number) * (abs(number) * (1 - delta))
