# System imports
from sys import exit

# Local imports
# from ..Save.save import Save
from ..Generator.generator import Generator
from ..Maze_Solver.recursive import Recursive


class Menu(object):

    # Initialization
    def __init__(self) -> None:
        self._option = 0
        self._id_txt = 0


    def __str__(self) -> str:
        return f'Option : {self._option}, \
                Id .txt : {self._id_txt}'


    def __repr__(self) -> str:
        return f'Menu(\'{self._option}\', \
                        {self._id_txt})'


    # Methods
    def display_menu(self) -> None:
         print("\nMENU :\n"
               "---------------------------\n"
               "1 : Diplay all solved mazes\n"
               "2 : Solve random maze -> recursive\n"
               "3 : Generate new maze\n"
               "4 : Exit\n"
               "---------------------------\n"
               "Your Choice : ", end = '')


    def launch_game(self) -> None:
        self.display_menu()
        while (True):
            self._option = input()
            match self._option:
                case '1':
                    print("\nNo save for the moment... :(")
                    # save = Save()
                    # save.display_database()
                    self.launch_game()
                case '2':
                    recursive = Recursive()
                    recursive.display_path()
                    self.launch_game()
                case '3':
                    generator = Generator()
                    self._id_txt = generator.get_current_id()
                    generator.generator(self._id_txt)
                    self._id_txt = generator.increment_current_id()
                    self.launch_game()
                case '4':
                    print("\nBye !")
                    exit(0)
                case _:
                    print("\nPlease choose a valid option :)")
                    self.display_menu()