import pyglet
from gui.gui import Gui

# window = pyglet.window.Window()

# label = pyglet.text.Label("Game")

# @window.event
# def on_draw():
#     window.clear()
#     label.draw()

def main():
    gui = Gui()
    gui.run()

if __name__ == "__main__":
    main()

