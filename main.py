from simple_term_menu import TerminalMenu
import os
from catapi import catapi
from dogapi import dogapi

def welcome():
    print(f"------------------------------------------------")
    print(f"Welcome to API JARVIS")
    print(f"------------------------------------------------")
def main():
    options = ["catapi", "dogapi"] 
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    print(f"You have selected {options[menu_entry_index]}!")
    if options[menu_entry_index] == 'catapi':
        catapi.catapi()
    elif options[menu_entry_index] == 'dogapi':
        dogapi.dogapi()
    os.system("clear")

if __name__ == "__main__":
    main()