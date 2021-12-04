

from services.battleservice import Battleservice

COMMANDS = {
    "x": "x return to main menu"
}

class Arenamenu:

    def __init__(self, io, battleservice):

        self._io = io
        self._battleservice = battleservice

    def print_commands(self):
        for command in COMMANDS:
            self._io.print(COMMANDS[command])

    def run(self):
        self._io.print("Arena")
        self._io.print(self._battleservice.enemy.name)
        self._io.print(self._battleservice.pc_weapon.name)
        self._io.print(self._battleservice.pc_weapon.size)

        while True:
            self.print_commands()
            command = self._io.read("command: ")
            if command not in COMMANDS:
                self._io.print("Invalid command")
            if command == "x":
                break