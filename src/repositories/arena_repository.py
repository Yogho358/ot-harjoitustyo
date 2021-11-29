import random
from entities.arena import Arena

class ArenaRepository:
    def __init__(self):
        pass

    def next_arena(self):
        if random.randint(0,1) == 0:
            return Arena("small")
        return Arena("big")

arena_repository = ArenaRepository()