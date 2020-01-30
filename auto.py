# button = mouse.scroll(0, 2)

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import sys


button = Button.left
# button = mouse.scroll(0, 2)
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                if(mode == 'a'):
                    mouse.click(self.button)
                elif(mode == 'b'):
                    mouse.scroll(0, -100)
                time.sleep(self.delay)


print('Start..')

try:
    print('Arg: '+sys.argv[1])
    mode = sys.argv[1]
except:
    print("# Please input arg for select mode between")
    print("#  `a` -> button left every 4sec")
    print("#  `b` -> scroll down every 4sec")
    sys.exit()

mouse = Controller()

if mode == 'a':
    delay = 4
elif mode == 'b':
    delay = 3

click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
            print("stop_clicking by click s")
        else:
            click_thread.start_clicking()
            print("start_clicking by click s")
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
        print("program stop.")


with Listener(on_press=on_press) as listener:
    print("program starting...")
    listener.join()
