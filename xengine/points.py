import numpy as np

from xengine.colors import  *
from xengine.types import   UNDEFINED

class Point(list):

    def __init__(self, x = 0, y = 0, z = 0, RGBA = WHITE):
        super().__init__([x, y, z, RGBA])

        self.vertices = np.array([x, y, z], dtype=np.float32)

        self.color = np.array([RGBA[0], RGBA[1], RGBA[2], RGBA[3]], dtype=np.float32)

        self.zoom = UNDEFINED

    def adapt_to_window(self, window = UNDEFINED, width = UNDEFINED, height = UNDEFINED):

        if window is not UNDEFINED:
            width = window.width
            height = window.height

        mid_width = width / 2
        mid_height = height / 2

        ratio = mid_height / mid_width

        if self.zoom is UNDEFINED:
            self.zoom = 1 / mid_width
        
        self.vertices = np.array([self.x * ratio * self.zoom, self.y * self.zoom, self.z * self.zoom], dtype=np.float32)

    def set_zoom(self, ratio):
        self.zoom = ratio

        self.vertices = np.array([self.x * ratio, self.y * ratio, self.z * ratio], dtype=np.float32)

    @property
    def x(self):
        return self.vertices[0]
    
    @property
    def y(self):
        return self.vertices[1]
    
    @property
    def z(self):
        return self.vertices[2]

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
