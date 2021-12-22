import pyglet
import time
from pyglet.window import key

class BattleUi:
    def __init__(self, battleservice):
        self._battleservice = battleservice

        self.pc = self._battleservice.pc
        self.enemy = self._battleservice.enemy


        self.window = pyglet.window.Window(fullscreen = True)
        self.main_label = pyglet.text.Label("Fight", 
                                            font_size = 40, 
                                            x=self.window.width//2, y=self.window.height-50,
                                            anchor_x="center", anchor_y="center"
                                            )

        self.arena_label = pyglet.text.Label(f"in a {self._battleservice.arena.size} arena",
                                            x=self.window.width//2, y=self.window.height-100,
                                            anchor_x="center", anchor_y="center")

        self.pc_label = pyglet.text.Label(f"{self.pc.name}, {self.pc.current_hp}/{self.pc.max_hp}", 
                                            x=50, y=self.window.height//8,
                                            anchor_x="center", anchor_y="center")

        self.enemy_label = pyglet.text.Label(f"{self.enemy.name}, {self.enemy.current_hp}/{self.enemy.max_hp}",
                                            x=self.window.width-100, y=self.window.height//8,
                                            anchor_x="center", anchor_y="center")

        
        self.report_label = pyglet.text.Label("",x=self.window.width//2, y=self.window.height//2,
                                            anchor_x="center", anchor_y="center")

        self.instruction_label = pyglet.text.Label("Press 1 to attack",x=self.window.width//2, y=self.window.height//7,
                                                    anchor_x="center", anchor_y="center")
        
        
        self.waiting_for_turn = False
        self.battle_over = False
        self.on_draw = self.window.event(self.on_draw)
        self.on_key_press = self.window.event(self.on_key_press)

    def on_draw(self):
        self.window.clear()
        if not self.battle_over:
            self.default_window()
        else:
            self.battle_over_window()

    def default_window(self):
        self.main_label.draw()
        self.pc_label.draw()
        self.enemy_label.draw()
        self.report_label.draw()
        self.arena_label.draw()
        self.instruction_label.draw()

    def battle_over_window(self):
        label = pyglet.text.Label("", 
                                    font_size = self.window.width//30, 
                                    x=self.window.width//2, y=self.window.height//2,
                                    anchor_x="center", anchor_y="center"
                                    )

        if self.pc.current_hp <= 0:
            label.text = "You died!"
        else:
            label.text = "You survived!"
        label.draw()
        pyglet.clock.schedule_once(self.close_window, 1)  

    def close_window(self, dt):
        self.window.close()                           
                        

    def on_key_press(self, symbol, modifiers):
        if self.waiting_for_turn:
            return
        if symbol == key._1:
            self.pc_attacks()

        self.update_labels()
        self.waiting_for_turn = True
        self.check_hps()
        pyglet.clock.schedule_once(self.enemy_turn, 1)
        

    def enemy_turn(self, dt):
        if self._battleservice.turn("npc", "attack"):
            self.report_label.text = "Enemy hits!"
        else:
            self.report_label.text = "Enemy misses!"

        self.update_labels()
        self.check_hps()
        self.waiting_for_turn = False
   
    def pc_attacks(self):
        if self._battleservice.turn("pc", "attack"):
            self.report_label.text = "You hit!"
        else:
            self.report_label.text = "You missed!"
        
    def check_hps(self):
        self.battle_over = self._battleservice.battle_over()
        

    def update_labels(self):
        self.pc_label.text = f"{self.pc.name}, {self.pc.current_hp}/{self.pc.max_hp}"
        self.enemy_label.text = f"{self.enemy.name}, {self.enemy.current_hp}/{self.enemy.max_hp}"

    def run(self):
        pyglet.app.run()