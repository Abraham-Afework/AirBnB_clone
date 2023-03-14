#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_quit(self, arg):
        """ Quit command to exit the program """
        exit(1)

    def do_EOF(self, arg):
       """ CTRL-D to exit the program """
       exit(1)
       print()
    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
