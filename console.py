#!/usr/bin/python3
import cmd
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""
class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is a command-line interface for some program.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        Usage: quit
        """
        exit(1)

    def do_EOF(self, arg):
       """
       EOF command to exit the program
       Usage: CTRL-D
       """
       exit(1)

    def emptyline(self):
        """
        Do nothing on empty input line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
