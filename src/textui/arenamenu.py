

from services.battleservice import Battleservice

COMMANDS = {
    "1": "1 attack",
    "x": "x return to main menu"
}

class Arenamenu:

    def __init__(self, io, battleservice):

        self._io = io
        self._battleservice = battleservice

    def _print_commands(self):
        for command in COMMANDS:
            self._io.print(COMMANDS[command])

    def enemy_turn(self):
        if self._battleservice.turn("npc", "attack"):
            self._io.print("Enemy hit!")
        else:
            self._io.print("Enemy missed!")

    def run(self):
        self._io.print("Arena")
        self._print_commands()

        while True:
            pc = self._battleservice.pc
            enemy = self._battleservice.enemy
            self._io.print(f"{pc.name}, {pc.current_hp}/{pc.max_hp} hitpoints, armed with {pc.weapon.name}")
            self._io.print("versus")
            self._io.print(f"{enemy.name}, {enemy.current_hp}/{enemy.max_hp} hitpoints, armed with {enemy.weapon.name}")

            if pc.current_hp <= 0:
                self._io.print("You died")
                break

            if enemy.current_hp <= 0:
                self._io.print("You won!")
                break

            command = self._io.read("command: ")
            if command not in COMMANDS:
                self._io.print("Invalid command")
                self._print_commands()
            if command == "x":
                break
            
            if command == "1":
                if self._battleservice.turn("pc", "attack"):
                    self._io.print("You hit!")
                else:
                    self._io.print("You missed!")
                self.enemy_turn()