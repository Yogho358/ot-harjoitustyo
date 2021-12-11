# import pyglet



# class Gui:
#     window = pyglet.window.Window()
#     label = pyglet.text.Label("Game")
#     @window.event
#     def on_draw():
#         window.clear()
#         label.draw()

#     def run():
#         pyglet.app.run()

import pyglet




class Gui:
    
    def __init__(self):
        self.window = pyglet.window.Window()
        self.label = pyglet.text.Label("Game")
        self.on_draw = self.window.event(self.on_draw)

    
    def on_draw(self):
        self.window.clear()
        self.label.draw()
        

    def run(self):
        pyglet.app.run()