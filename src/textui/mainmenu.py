from services.battleservice import Battleservice
from services.gameservice import gameservice
from entities.character import Character
from textui.arenamenu import Arenamenu

COMMANDS = {
    "x": "x quit",
    "1": "1 New character",
    "2": "2 Load character",
    "3": "3 enter arena"
}


class Mainmenu:
    def __init__(self, io, gameservice):
        self.io = io
        self.gameservice = gameservice
        self.player_char = None
        

    def run(self):
        self.io.print("Welcome to the Game")
        self.print_commands()

        while True:
            self.player_char = self.gameservice.player_char
            if self.player_char == None:
                self.io.print("No character selected")
            else:
                self.io.print(f"{self.player_char.name} ready for adventure")
                self.io.print(f"You are about to face {self.gameservice.get_enemy().name} in a {self.gameservice.get_arena().size} arena")
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                self.io.print("Invalid command")
                self.print_commands()
            if command == "x":
                break

            if command == "1":
                self.create_pc()

            if command == "2":
                self.select_pc()

            if command == "3":
                try:
                    battleservice = self.gameservice.enter_arena()
                    arenamenu = Arenamenu(self.io, battleservice)
                    arenamenu.run()
                except Exception as e:
                    self.io.print(e)

    def print_commands(self):
        for command in COMMANDS:
            self.io.print(COMMANDS[command])

    def create_pc(self):
        name = self.io.read("name: ")
        try:
            self.gameservice.create_character(
                name=name, current_hp=20, max_hp=20, weapon="sword", pc_or_npc="pc")
        except Exception as e:
            self.io.print(e)

    def select_pc(self):
        chars = self.gameservice.find_all()
        if len(chars) == 0:
            self.io.print("No characters available")
            return
     
        for i in range(len(chars)):
            self.io.print(f"{i+1}: {chars[i].name}")
        try:
            choice = int(self.io.read("number of choice: "))
        except ValueError:
            self.io.print("Must give a number")
            return
        char = chars[choice-1].name
        self.gameservice.set_player_char(char)     

