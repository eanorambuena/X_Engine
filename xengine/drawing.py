import glfw as gl# pip install glfw
import eggdriver as ed

WIDTH, HEIGHT = 720, 480
TITLE = "XEngine App"
MONITOR = None
SHARE = None

def main():

    if not gl.init(): # Initialize the window
        return

    window = gl.create_window(WIDTH, HEIGHT, TITLE, MONITOR, SHARE)

    if not window:
        gl.terminate()
        return

    gl.make_context_current(window) # Make the window the principal window

    while not gl.window_should_close(window):
        # Drawing zone START

        # Drawing zone END

        gl.swap_buffers(window) # Swap the Drawing buffer with the Display buffer

        gl.poll_events() # Verify events are correct

    gl.terminate() # Close

main()