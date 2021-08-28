from contact import Contact

from json import loads, dumps
from pathlib import Path
from sys import exit as die
from re import findall
from time import sleep
from typing import Union, Generator
from asyncio import run as async_run


class Main:
    """
    ATTRIBUTES
    ----------------
    PRIVATE | __CONTACTS_DIR : str
    PRIVATE | __MENU_ITEMS : tuple[str, ...]
    PRIVATE | __NUMBER_REGEX: str

    METHODS
    ---------------
    PRIVATE | __new__ -> object
    PRIVATE | __init__ -> None
    PRIVATE | __str__ -> str

    PUBLIC | run -> None
    PRIVATE | _menu -> None
    PRIVATE | _display -> None
    PRIVATE | _create -> None
    PRIVATE | _delete -> None
    PRIVATE | _save -> None
    PRIVATE | _load -> list or dict
    PUBLIC | read_json -> list or dict
    PUBLIC | write_file -> None
    """

    # file directories
    __CONTACTS_DIR: str = r"./contacts.json"

    # tuples
    __MENU_ITEMS: tuple[str, ...] = ("View Contacts", "New Contact", "Delete Contact")

    # regex's
    __NUMBER_REGEX: str = r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"

    def __new__(cls) -> object:
        """
        Is ran when an instance of the class is created.

        :return: object
        """

        return object.__new__(cls)

    def __init__(self) -> None:
        """
        Is ran when an instance of the class is created.
        Initialises a list of all saved contacts.

        :return: None
        """

        self._contacts: list[Contact] = list(self._load())  # A list of all saved contacts

    def __str__(self) -> str:
        """
        Returns information about the class.

        :return: str
        """

        return f"Main class. Reading from: {self.__CONTACTS_DIR}"

    def run(self) -> None:
        """
        Is ran to start program.

        :return: None
        """

        self._menu()

    def _menu(self) -> None:
        """
        Displays a menu for the user to select what they would like to do.

        :return: None
        """

        while 1:
            sleep(1)
            print("\nPlease enter the number of the function you would like to execute: ")
            for index, item in enumerate(self.__MENU_ITEMS):  # displays all menu items
                print(f"\t[{index+1}] {item}")
            sleep(1)

            try:
                """
                Checks if user entered a valid number,
                Then runs correct function or displays error message.
                """
                match int(input()):
                    case 1:
                        self._display()
                    case 2:
                        self._create()
                    case 3:
                        self._delete()
                    case _:
                        print("ERROR: Invalid function number. Please try again...")
            except ValueError:  # if user didn't enter a number
                print("ERROR: Invalid function number. Please try again...")

    def _display(self) -> None:
        """
        Displays a list of saved contacts.

        :return: None
        """

        if self._contacts:  # if the list is not empty
            print("\nCONTACTS:")
            for index, item in enumerate(self._contacts):  # display contacts
                print(f"\tName: {item.name}\n\tNumber: {item.num}\n\tAddress: {item.addr}")
                print() if index != len(self._contacts)-1 else None
        else:
            print("ERROR: No contacts exist. Create a contact...")

    def _create(self) -> None:
        """
        Displays menu for user to create new contact.

        :return: None
        """

        print("\nNEW CONTACT:")

        while 1:  # get input for 'name' until valid input is given
            name: str = input("\tEnter name of contact: ").title()
            if not name:  # check if 'name' is empty
                print("\n\tERROR: Name is empty. Please try again...\n")
            else:
                break

        while 1:
            num: str = input("\tEnter number of contact: ")
            if not num:
                print("\n\tERROR: Contact number is empty. Please try again...\n")
            elif not findall(self.__NUMBER_REGEX, num):  # match against regex to check for correct formatting
                print("\n\tERROR: Contact number is not in correct format (correct formats are '07XXXXXXXXX' or '+447XXXXXXXXX'). Please try again...\n")
            else:
                break

        while 1:
            addr: str = input("\tEnter address of contact: ").title()
            if not addr:
                print("\n\tERROR: Address is empty. Please try again...\n")
            else:
                break
        
        self._contacts.append(Contact(name, num, addr))  # append new instance of class 'Contact' to list
        async_run(self._save())  # save to file

    def _delete(self) -> None:
        """
        Displays menu for user to choose which contact to delete.

        :return: None
        """

        print("\nEnter the number of the contact you would like to delete:")
        for index, item in enumerate(self._contacts):  # display name of all contacts
            print(f"\t[{index+1}] {item.name}")

        try:
            index = int(input())-1
  
        except ValueError:
            print("ERROR: Invalid contact number. Please try again...")
        
        finally:
            if index <= len(self._contacts):
                self._contacts.pop(index)  # remove contact from list
                async_run(self._save())  # save to file
            else:
                print("ERROR: Invalid contact number. Please try again...")

<<<<<<< HEAD
        except ValueError:  # if a number isn't entered
            print("ERROR: Invalid contact number. Please try again...")

    async def _save(self) -> None:
        """
        Saves contacts to savefile.
        Asynchronous.

        :return: None
        """

        async_run(self.write_file(self.__CONTACTS_DIR, (repr(self._contacts[index]) for index, _ in enumerate(self._contacts))))

    def _load(self) -> Generator[Contact]:
        """
        Loads the contents of the savefile.
=======
    def _save(self) -> None:
        self._write_file(self.__CONTACTS_DIR, dumps(list(repr(self._contacts[index]) for index, _ in enumerate(self._contacts)), sort_keys=True, indent=4))
>>>>>>> 362e687603ff4f558bd8b984a5ffb44e23a21387

        :return: Generator[Contact]
        """

        for item in self.read_json(self.__CONTACTS_DIR):  # loop through savefile
            yield eval(item)  # return generator containing instances of 'Contact'

    @classmethod
    def read_json(cls, path: str) -> Union[list, dict]:
        """
        Returns JSON data from a specified file if the file exists.
        Else exits program and displays error.

        :param str path: The directory to read the JSON data from.

        :return: Union[list, dict]
        """

        return loads(open(path, "r").read()) if Path(path).is_file() else die("FATAL ERROR: File '{path}', does not exist...")

    @classmethod
    async def write_file(cls, path: str, data: Union[list, dict, Generator]) -> None:
        """
        Writes JSON data to a specified file.
        Asynchronous.

        :param str path: The directory to write the file to.
        :param str data: The data to write to the file.

        :return: None
        """

        open(path, "w").write(dumps(data, sort_keys=True, indent=4))


def run() -> None:
    """
    Create instance of 'Main' class.
    Run 'Main' class.

    :return: None
    """

    main: Main = Main()
    main.run()


if __name__ == "__main__":
    run()
