#!/usr/bin/python3
"""
    Main Console program
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class represents a command-line interface for a program.
    It inherits from the cmd.Cmd class, which provides a framework for building
    line-oriented command interpreters.
    """

    prompt = "(hbnb) "
    count = 0

    def my_errors(self, line, num_of_args):
        """
        The my_errors method validates the user input and displays error mesgs
        to the user if there are any errors.

        Parameters:
        - line: the input line
        - num_of_args: the expected number of arguments

        Returns:
        - 0 if there are no errors
        - 1 if there are errors

        """
        classes = ["BaseModel", "State", "Place",
                   "Amenity", "City", "Review", "User"]

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return 1

        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1

        elif num_of_args == 1:
            return 0

        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1

        data = models.storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")

        key = args[0] + '.' + args[1]

        if num_of_args >= 2 and key not in data:
            print(msg[3])
            return 1

        elif num_of_args == 2:
            return 0
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1

        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1

        return 0

    def do_quit(self, arg):
        """
        The do_quit method allows the user to exit the program.

        Parameters:
        - arg: any arguments passed to the method (ignored)

        """
        exit(1)

    def do_EOF(self, arg):
        """
        The do_EOF method allows the user to exit the program by typing Ctrl-D.

        Parameters:
        - arg: any arguments passed to the method (ignored)

        """
        exit(1)

    def emptyline(self):
        """
        The emptyline method does nothing when the user inputs an empty line.

        Parameters:
        - None

        """
        pass

    def do_show(self, line):
        """
        This method retrieves an instance based on its ID.
        Usage: show <class name> <id>
        """

        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        data = models.storage.all()

        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        print(data[key])

    def do_create(self, line):
        """
        This method creates a new instance of a class and
        saves it to JSON file.
        Usage: create <class name>
        """

        if (self.my_errors(line, 1) == 1):
            return
        args = line.split(" ")

        new_obj = eval(args[0])()
        new_obj.save()
        print(new_obj.id)

    def do_destroy(self, line):
        """
        This method deletes an instance based on its ID.
        Usage: destroy <class name> <id>
        """

        if (self.my_errors(line, 2) == 1):
            return
        args = line.split()
        data = models.storage.all()
        if args[1][0] == '"':
            args[1] = args[1].replace('"', "")
        key = args[0] + '.' + args[1]
        if data[key] in data.values():
            del data[key]
        models.storage.save()

    def do_all(self, line):
        """
        This method prints all instances of a class or all instances
        if no class is specified.
        Usage: all [<class name>]
        """

        data = models.storage.all()
        input_data = line.split()
        if not line:
            for value in data.values():
                self.count += 1
                print(str(value))
        elif (self.my_errors(line, 1) == 1):
            return
        else:
            for value in data.values():
                if value.__class__.__name__ == input_data[0]:
                    self.count += 1
                    print(str(value))

    def do_update(self, line):
        """
        This method updates an instance based on its ID.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        if (self.my_errors(line, 4) == 1):
            return

        input_data = line.split()
        storage_data = models.storage.all()

        for i in range(len(input_data[1:]) + 1):
            if input_data[i][0] == '"':
                input_data[i] = input_data[i].replace('"', "")
        key = input_data[0] + '.' + input_data[1]
        attr_k = input_data[2]
        attr_v = input_data[3]
        try:
            if attr_v.isdigit():
                attr_v = int(attr_v)
            elif float(attr_v):
                attr_v = float(attr_v)
        except ValueError:
            pass
        class_attr = type(storage_data[key]).__dict__

        if attr_k in class_attr.keys():
            try:
                attr_v = type(class_attr[attr_k])(attr_v)
            except Exception:
                print("Entered wrong value type")
                return

        setattr(storage_data[key], attr_k, attr_v)
        models.storage.save()

    def default(self, line):
        """
            A method that handles the input commands that are not recognized by
            the existing commands.  It parses the input line to extract the
            method name and arguments, checks if the method name is valid,
        """
        methods = ["BaseModel", "User", "State",
                   "City", "Amenity", "Place", "Review"]

        """ A list of valid method names """
        commands = {
            "all()": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        args = line.split('.')

        """ Splits the input line by the period (.) separator"""

        if args[0] in methods:
            """ Checks if the first argument (method name) is valid """
            if args[1] in ["all()", "count"]:

                commands[args[1]](args[0])
            elif args[1] in ["show", "destroy"]:

                commands[args[1]](args[0])
            elif args[1] == "update":

                print("wow")
            else:
                print("*** Unknown syntax: {}".format(line))

    def do_count(self, line):
        """
            A method that counts the number of objects of a given
            class in the data store.
            It extracts the class name from the input
            line and iterates over all objects in the data store,
            incrementing a counter for each object whose class name matches
            the given class name. Finally, it prints the counter value.
        """
        self.count = 0
        """ Initializes the counter """
        data = models.storage.all()
        """ Retrieves all objects from the data store """
        input_data = line.split()
        """ Splits the input line by the whitespace separator """
        for value in data.values():
            if value.__class__.__name__ == input_data[0]:
                """ Checks if the class name of the object
                matches the given class name """

                self.count += 1
                """ Increments the counter """
        print(self.count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
