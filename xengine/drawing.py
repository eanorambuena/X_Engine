from turtle import width
import  numpy as np
from    OpenGL.GL import (
    glColorPointer,
    glEnableClientState,
    glVertexPointer,
    GL_COLOR_ARRAY,
    GL_FLOAT,
    GL_VERTEX_ARRAY
) # pip install PyOpenGL

from xengine.colors import  *
from xengine.types import   UNDEFINED
from xengine.windows import Window

class Point(list):

    def __init__(self, x = 0, y = 0, z = 0, RGBA = WHITE):
        super().__init__([x, y, z, RGBA])

        self.verteces = np.array([x, y, z], dtype=np.float32)

        self.color = np.array([RGBA[0], RGBA[1], RGBA[2], RGBA[3]], dtype=np.float32)

    def adapt_to_window(self, window = UNDEFINED, width = UNDEFINED, height = UNDEFINED):

        if window is not UNDEFINED:
            mid_width = window.width / 2
            mid_height = window.height / 2

        else:
            mid_width = width / 2
            mid_height = height / 2

        self.verteces = np.array([self.x / mid_width, self.y / mid_height, self.z], dtype=np.float32)

    @property
    def x(self):
        return self.verteces[0]
    
    @property
    def y(self):
        return self.verteces[1]
    
    @property
    def z(self):
        return self.verteces[2]

    @property
    def R(self):
        return self.color[0]

    @property
    def G(self):
        return self.color[1]
    
    @property
    def B(self):
        return self.color[2]

    @property
    def A(self):
        return self.color[3]

class Triangle(list):

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.initialize_triangle(point_1, point_2, point_3)
    
    def initialize_triangle(self, point_1: Point, point_2: Point, point_3: Point):
        super().__init__([point_1, point_2, point_3])

        self.verteces = np.array([  point_1.x, point_1.y, point_1.z,
                                    point_2.x, point_2.y, point_2.z,
                                    point_3.x, point_3.y, point_3.z],
                                    dtype=np.float32)

        self.colors = np.array([point_1.R, point_1.G, point_1.B, point_1.A,
                                point_2.R, point_2.G, point_2.B, point_2.A,
                                point_3.R, point_3.G, point_3.B, point_3.A],
                                dtype=np.float32)

    def adapt_to_window(self, window = UNDEFINED, width = UNDEFINED, height = UNDEFINED):
        point1: Point = self[0]
        point2: Point = self[1]
        point3: Point = self[2]

        if window is not UNDEFINED:
            point1.adapt_to_window(window)
            point2.adapt_to_window(window)
            point3.adapt_to_window(window)

        else:
            point1.adapt_to_window(width = width, height = height)
            point2.adapt_to_window(width = width, height = height)
            point3.adapt_to_window(width = width, height = height)

        self.initialize_triangle(point1, point2, point3)

    def draw(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.verteces)

        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(4, GL_FLOAT, 0, self.colors)

