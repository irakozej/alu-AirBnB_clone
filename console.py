#!/usr/bin/python3
import cmd
import shlex
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    valid_classes = ["BaseModel"]


    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """
        Quit the program
        """
        return True
    
    def help_quit(self, arg):
        """
        Displays information about the quit command.
        """
        print("quit command to exit the program")

    def do_EOF(self, arg):
        """
        Handle the End-of-file (Ctrl+D) event to exit the program.
        """
        print()
        return True
    
    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file and prints the id.
        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing**")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <slass_name> <id>
        """
        pass

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        pass

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: all <class_name>
        """
        pass

    def do_update(self, arg):
    
if __name__ == "__main__":
    HBNBCommand().cmdloop()