import sys
import termios
import tty
import signal

class InputHandler:
    def __init__(self):
        self.current_key = None

    def setup_input(self):
        # Save the terminal settings
        self.old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def restore_input(self):
        # Restore the terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.old_settings)

    def read_input(self):
        # Read single character without pressing enter
        return sys.stdin.read(1)

    def signal_handler(self, signum, frame):
        # Handle any cleanup on unexpected exit
        self.restore_input()
        sys.exit(0)

    def __enter__(self):
        self.setup_input()
        signal.signal(signal.SIGINT, self.signal_handler)
        return self

    def __exit__(self, type, value, traceback):
        self.restore_input()
