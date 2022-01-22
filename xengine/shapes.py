import ctypes
import  numpy as np

from    OpenGL.GL import (
    glBindBuffer,
    glBufferData,
    glColorPointer,
    glEnableClientState,
    glEnableVertexAttribArray,
    glGenBuffers,
    glGetAttribLocation,
    glUseProgram,
    glVertexAttribPointer,
    glVertexPointer,
    GL_ARRAY_BUFFER,
    GL_COLOR_ARRAY,
    GL_FALSE,
    GL_FLOAT,
    GL_FRAGMENT_SHADER,
    GL_STATIC_DRAW,
    GL_VERTEX_ARRAY,
    GL_VERTEX_SHADER,
) # pip install PyOpenGL

from    OpenGL.GL.shaders import (
    compileShader,
    compileProgram
)

from xengine.colors import  *
from xengine.points import  Point
from xengine.types import   UNDEFINED

BYTES_PER_FLOAT = 4

class Triangle(list):

    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.initialize_triangle(point_1, point_2, point_3)
    
    def initialize_triangle(self, point_1: Point, point_2: Point, point_3: Point):
        super().__init__([point_1, point_2, point_3])

        self.vertices = np.array([  point_1.x, point_1.y, point_1.z,
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
        glVertexPointer(3, GL_FLOAT, 0, self.vertices)

        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(4, GL_FLOAT, 0, self.colors)

class GeneralShape(list):

    def __init__(self, *points: Point):
        points_list = list(points)

        self.initialize_general_shape(points_list)

    def initialize_general_shape(self, points_list):
        super().__init__(points_list)

        points = len(points_list)

        vertices = []

        for i in range(points):
            point = points_list[i]

            vertices.append(point.x)
            vertices.append(point.y)
            vertices.append(point.z)
            vertices.append(point.R)
            vertices.append(point.G)
            vertices.append(point.B)
            vertices.append(point.A)

        self.vertices = np.array(vertices, dtype=np.float32)

    def adapt_to_window(self, window = UNDEFINED, width = UNDEFINED, height = UNDEFINED):

        new_points = []

        for point in self:

            if window is not UNDEFINED:
                point.adapt_to_window(window)

            else:
                point.adapt_to_window(width = width, height = height)

            new_points.append(point)

        self.initialize_general_shape(new_points)

    def set_shader(self, vertex_shader, fragment_shader):
        compiled_vertex_shader = compileShader(vertex_shader, GL_VERTEX_SHADER)
        compiled_fragment_shader = compileShader(fragment_shader, GL_FRAGMENT_SHADER)

        self.shader = compileProgram(compiled_vertex_shader, compiled_fragment_shader)

    def draw(self):
        VBO = glGenBuffers(1)

        glBindBuffer(GL_ARRAY_BUFFER, VBO)

        number_of_bytes = len(self.vertices) * BYTES_PER_FLOAT

        glBufferData(GL_ARRAY_BUFFER, number_of_bytes, self.vertices, GL_STATIC_DRAW)

        position_coords = len("xyz")
        color_coords = len("RGBA")
        total_coords = position_coords + color_coords

        position = glGetAttribLocation(self.shader, "a_position")
        glEnableVertexAttribArray(position)
        position_pointer = ctypes.c_void_p(0)
        glVertexAttribPointer(position, position_coords, GL_FLOAT, GL_FALSE, total_coords * BYTES_PER_FLOAT, position_pointer)

        color = glGetAttribLocation(self.shader, "a_color")
        glEnableVertexAttribArray(color)
        color_pointer = ctypes.c_void_p(position_coords * BYTES_PER_FLOAT)
        glVertexAttribPointer(color, color_coords, GL_FLOAT, GL_FALSE, total_coords * BYTES_PER_FLOAT, color_pointer)

        glUseProgram(self.shader)
