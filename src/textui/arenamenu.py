

from services.battleservice import Battleservice

COMMANDS = {
    "x": "x return to main menu"
}

class Arenamenu:

    def __init__(self, io, battleservice):

        self._io = io
        self._battleservice = battleservice

    def _print_commands(self):
        for command in COMMANDS:
            self._io.print(COMMANDS[command])

    def run(self):
        self._io.print("Arena")

        while True:
            pc = self._battleservice.pc
            enemy = self._battleservice.enemy
            self._io.print(f"{pc.name}, {pc.current_hp}/{pc.max_hp} hitpoints, armed with {pc.weapon}")
            self._io.print("versus")
            self._io.print(f"{enemy.name}, {enemy.current_hp}/{enemy.max_hp} hitpoints, armed with {enemy.weapon}")
            command = self._io.read("command: ")
            if command not in COMMANDS:
                self._io.print("Invalid command")
                self._print_commands()
            if command == "x":
                break