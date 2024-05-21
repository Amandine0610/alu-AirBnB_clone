#!/usr/bin/python3
"""
Defines the command interpreter for the AirBnB clone project.
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse_arguments(arg):
    """
    Parse a given argument string and return a list of arguments.
    """
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class AirBnBCommand(cmd.Cmd):
    """
    Defines the command interpreter for AirBnB.
    """

    prompt = "(hbnb) "
    available_classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """
        Override the emptyline method to do nothing.
        """
        pass

    def default(self, arg):
        """
        Default behavior for unknown commands.
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict:
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """
        print("")
        return True

    def do_create(self, arg):
        """
        Create a new class instance and print its id.
        Usage: create <class>
        """
        argl = parse_arguments(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in AirBnBCommand.available_classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Display the string representation of a class instance of a given id.
        Usage: show <class> <id> or <class>.show(<id>)
        """
        argl = parse_arguments(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in AirBnBCommand.available_classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Delete a class instance of a given id.
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        argl = parse_arguments(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in AirBnBCommand.available_classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        Usage: all or all <class> or <class>.all()
        """
        argl = parse_arguments(arg)
        if len(argl) > 0 and argl[0] not in AirBnBCommand.available_classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class.
        Usage: count <class> or <class>.count()
        """
        argl = parse_arguments(arg)
        count = sum(1 for obj in storage.all().values() if argl[0] == obj.__class__.__name__)
        print(count)

    def do_update(self, arg):
        """
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        Usage: update <class> <id> <attribute_name> <attribute_value> or
               <class>.update(<id>, <attribute_name>, <attribute_value>) or
               <class>.update(<id>, <dictionary>)
        """
        argl = parse_arguments(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in AirBnBCommand.available_classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        obj = objdict["{}.{}".format(argl[0], argl[1])]
        if len(argl) == 4:
            if argl[2] in obj.__class__.__dict__:
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif isinstance(eval(argl[2]), dict):
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__ and
                        isinstance(obj.__class__.__dict__[k], (str, int, float))):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    AirBnBCommand().cmdloop()

