from entities.character import Character

class Character_Repository:
    def __init__(self):
        self.characters = []

    def find_all(self):
        return self.characters

    def create(self,character):
        characters = self.find_all()
        existing_character = None
        for c in characters:
            if c.name == character.name:
                existing_character = c
    
        if existing_character:
            raise Exception(f"Character with name {character.name} already exists")
        characters.append(character)
        self.characters = characters
        return character

    def find_by_character_name(self, name):
        character = None
        for c in self.characters:
            if c.name == name:
                character = c
                return character

        if character == None:
            raise Exception(f"{name} not found")

    def clear(self):
        self.characters = []

character_repository = Character_Repository()
        
