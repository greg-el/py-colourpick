from Xlib import X, display, Xutil

class Window(object):
    def __init__(self, display):
        self.d = display
        self.root = self.d.screen().root
        data = self.root.query_pointer()
        

    def loop(self):
        while True:
            event = self.d.next_event()
            print(event)
            if event.type == X.KeyPress:
                exit(1)
        


if __name__ == "__main__":
    test = Window(display.Display())
    test.loop()