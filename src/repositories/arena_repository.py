import random
from entities.arena import Arena

class ArenaRepository:
    """Placeholder for a future time when different arenas are saved in database
    """
    def __init__(self):
        pass

    def next_arena(self):
        if random.randint(0,1) == 0:
            return Arena("small")
        return Arena("large")

arena_repository = ArenaRepository()
