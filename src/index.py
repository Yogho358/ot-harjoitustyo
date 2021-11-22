from textui.consoleio import ConsoleIO
from textui.mainmenu import Mainmenu
from services.gameservice import gameservice

def main():
    io = ConsoleIO
    mainmenu = Mainmenu(io, gameservice)
    mainmenu.run()



if __name__ == "__main__":
    main()