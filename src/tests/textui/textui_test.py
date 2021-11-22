import unittest
from textui.mainmenu import Mainmenu

class StubIO:
    def __init__ (self,inputs):
        self.inputs = inputs
        self.outputs = []
    
    def read(self, text):
        return self.inputs.pop(0)

    def print(self, text):
        self.outputs.append(text)

class TestTextUi(unittest.TestCase):

    def test_main_menu_opens(self):
        io = StubIO(["x"])
        menu = Mainmenu(io)
        menu.run()
        self.assertEqual(("Welcome to the Game" in io.outputs), True)