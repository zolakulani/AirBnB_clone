#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage

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
    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = globals()[args]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

        def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id."""
            args = args.split()
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                class_name, instance_id = args[0], args[1]
                if class_name not in globals():
                    print("** class doesn't exist **")
                else:
                    key = "{}.{}".format(class_name, instance_id)
                    instance = storage.all().get(key)
                    if instance is None:
                        print("** no instance found **")
                    else:
                        print(instance)

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
                print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            if class_name not in globals():
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                   print("** no instance found **")
                else:
                   del storage.all()[key]
                   storage.save()
    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name."""
        if args:
            if args not in globals():
                print("** class doesn't exist **")
                return
            class_name = args
            instances = [str(obj) for key, obj in storage.all().items() if key.startswith(class_name)]
        else:
            instances = [str(obj) for obj in storage.all().values()]
        print(instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = args.split()
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            else:
                print("** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args[0], args[1], args[2], args[3]
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(class_name, instance_id)
        instance = storage.all().get(key)
        if instance is None:
            print("** no instance found **")
        else:
            try:
                attr_value = eval(attr_value)  # Cast the attribute value
            except (SyntaxError, NameError):
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
    # Add other commands and functionality as needed


if __name__ == '__main__':
    HBNBCommand().cmdloop()
