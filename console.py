#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '  # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    # Add other commands and functionality as needed

if __name__ == '__main__':
    HBNBCommand().cmdloop()
