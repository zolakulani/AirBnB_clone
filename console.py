#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '  # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)"""
        return True

    # Add other commands and functionality as needed

if __name__ == '__main__':
    HBNBCommand().cmdloop()
