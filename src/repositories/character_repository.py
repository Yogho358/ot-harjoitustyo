#from entities.character import Character

class CharacterRepository:
    def __init__(self):
        self.characters = []

    def find_all(self):
        return self.characters

    def create(self, character):
        characters = self.find_all()
        existing_character = None
        for char in characters:
            if char.name == character.name:
                existing_character = char

        if existing_character:
            raise Exception(
                f"Character with name {character.name} already exists")
        characters.append(character)
        self.characters = characters
        return character

    def find_by_character_name(self, name):
        character = None
        for char in self.characters:
            if char.name == name:
                character = char


        if character is None:
            raise Exception(f"{name} not found")

        return character

    def clear(self):
        self.characters = []


character_repository = CharacterRepository()
