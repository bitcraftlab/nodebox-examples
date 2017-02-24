""" turtle commands for nodebox 3 """

# @bitcraftlab 2017

from math import sin, cos
from nodebox.graphics import Point, Path, Color
from nodebox.util.Geometry import radians

# extending the path class of nodebox, so we can construct a path with turtle commands

class Turtle(Path):

    def __init__(self, pos, dir):

        # position and direction of the turtle
        self.pos = pos
        self.dir = dir

        # thin black path by default
        self.setStroke(Color.BLACK)
        self.setStrokeWidth(1)
        self.setFill(None)

        # start path
        self.moveto(self.pos.x, self.pos.y)

    #def __repr__(self):
        #return u"Turtle %i : pos: (%f,%f) dir: %f" % (id(self), self.pos.x, self.pos.y, self.dir)

    def left(self, angle):
        self.dir -= angle

    def right(self, angle):
        self.dir += angle

    def forward(self, distance):
        x = self.pos.x + distance * cos(radians(self.dir))
        y = self.pos.y + distance * sin(radians(self.dir))
        p = Point(x, y)
        self.pos = p
        # extend the path
        self.lineto(p.x, p.y)

################################################################################

def create(pos=[0, 0], ang = 0):
    turtle = Turtle(pos, ang)
    return turtle

def left(turtle, ang):
    turtle.left(ang)
    return turtle

def right(turtle, ang):
    turtle.right(ang)
    return turtle

def forward(turtle, steps):
    turtle.forward(steps)
    return turtle
