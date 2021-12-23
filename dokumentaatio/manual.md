### User manual

## Set up

First of all, run command "poetry install" to finish installation, and run command "poetry run invoke build" to set up databases. Database name can be manually changed in the .env file.

## Start
Start the program with the command "poetry run invoke start"

## Playing the game

The game opens to a command line main menu. There is a default character, Mr X, in the database ready, so you can choose that, or create a new character. You can also see the enemy type you are going to fight, randomized from existing types (currently 2 types), and the size of the arena.

The size of the arena affects how different sized weapons work, and also different skills might give different modifiers based on the arena size.

Once your character is ready, you can start the battle by entering the arena.

The battle is turn based and runs on a separate battle ui. Currently you can either make a default attack by pressing a, or if you have skills, the ui will show you how to use a skill. Currently the ui supports up to five skills. Mr X has one skill in the beginning, newly created characters don't have skills. If you win a fight either by an overwhelming victory or by barely making it out alive, you get a chance to learn a new skill. What skills are available depends on which weapon you used.

Currently there are following skills:
- Half swording for longsword, makes it easier to manouver the sword in small spaces.
- Overhead swing for longsword, gives malus for chance to hit but increases damage a lot, can only be used effectively in large spaces.
- Double stab for short swords, gives damage bonus in small spaces.
- Off-hand distraction for short swords, gives hit bonus but damage malus in all arenas.

Currently there is no feature to add more weapons or skills through the ui, but it can be done easily enough by modifying the file initalise_database.py.

The enemy will always take a turn after you choose the action for yourself. After the fight your character's state is automatically saved, and if the character is dead, it can't be used anymore.

