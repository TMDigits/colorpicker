from PIL import ImageGrab

from pynput import mouse


class Picker():
    def __init__(self):
        self.ctrl = mouse.Controller()

    def get_color(self):
        pos = self.ctrl.position
        img = ImageGrab.grab().load()
        return img[pos[0], pos[1]]
