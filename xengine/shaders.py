STANDARD_VERTEX_SHADER = """
# version 330 core

in vec3 a_position;
in vec4 a_color;

out vec4 v_color;

void main() {
    gl_Position = vec4(a_position, 1.0);
    v_color = a_color;
}
"""

STANDARD_FRAGMENT_SHADER = """
# version 330 core

in vec4 v_color;

out vec4 out_color;

void main() {
    out_color = v_color;
}
"""

STANDARD_SHADER = (STANDARD_VERTEX_SHADER, STANDARD_FRAGMENT_SHADER)

class Shader:

    def __init__(self, vertex_shader = STANDARD_VERTEX_SHADER, fragment_shader = STANDARD_FRAGMENT_SHADER):
        self.vertex_shader = vertex_shader
        self.fragment_shader = fragment_shader
