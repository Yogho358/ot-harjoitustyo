from services.gameservice import gameservice
from entities.character import Character

COMMANDS = {
    "x": "x quit",
    "1": "1 New character",
    "2": "2 Load character",
}

class Mainmenu:
    def __init__(self,io,gameservice):
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
            command = self.io.read("Command: ")
            if not command in COMMANDS:
                self.io.print("Invalid command")
                self.print_commands()
            if command == "x":
                break
            if command == "1":
                name = self.io.read("name: ")
                self.gameservice.create_character(name = name, current_hp = 20, max_hp = 20, weapon = "sword")
            
            if command == "2":
                chars = self.gameservice.find_all()
                for i in range(len(chars)):
                    self.io.print(f"{i+1}: {chars[i].name}")
                choise = int(self.io.read("number of choise: "))
                char = chars[choise-1].name
                self.gameservice.set_player_char(char)



    def print_commands(self):
        for command in COMMANDS:
            self.io.print(command)