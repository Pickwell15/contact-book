from contact import Contact

from json import loads, dumps
from pathlib import Path
from sys import exit as die
from re import findall


class Main:

    __CONTACTS_DIR: str = "./contacts.json"

    __MENU_ITEMS: list[str] = ["View Contacts", "New Contact", "Delete Contact"]

    __NUMBER_REGEX: str = r"^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$"

    def __new__(cls) -> object:
        return object.__new__(cls)

    def __init__(self) -> None:
        self._contacts: list[Contact] = list(self._load())

    def __str__(self) -> str:
        return f"Main class. Reading from: {self.__CONTACTS_DIR}"

    def run(self) -> None:
        self._menu()

    def _menu(self) -> None:
        while 1:
            print("\nPlease enter the number of the function you would like to execute: ")
            for index, item in enumerate(self.__MENU_ITEMS):
                print(f"\t[{index+1}] {item}")
            try:
                match int(input()):
                    case 1:
                        self._display()
                    case 2:
                        self._create()
                    case 3:
                        self._delete()
                    case _:
                        print("ERROR: Invalid function number. Please try again...")
            except ValueError:
                print("ERROR: Invalid function number. Please try again...")

    def _display(self) -> None:
        if self._contacts:
            print("\nCONTACTS:")
            for index, item in enumerate(self._contacts):
                print(f"\tName: {item.name}\n\tNumber: {item.num}\n\tAddress: {item.addr}")
                print() if index >= 0 else None
        else:
            print("ERROR: No contacts exist. Create a contact...")

    def _create(self) -> None:
        print("\nNEW CONTACT:")

        while 1:
            name: str = input("\tEnter name of contact: ").title()
            if not name:
                print("\n\tERROR: Name is empty. Please try again...\n")
            else:
                break

        while 1:
            num: str = input("\tEnter number of contact: ")
            if not num:
                print("\n\tERROR: Contact number is empty. Please try again...\n")
            elif findall(self.__NUMBER_REGEX, num):
                break
            else:
                print("\n\tERROR: Contact number is not in correct format (correct formats are '07XXXXXXXXX' or '+447XXXXXXXXX'). Please try again...\n")

        while 1:
            addr: str = input("\tEnter address of contact: ").title()
            if not addr:
                print("\n\tERROR: Address is empty. Please try again...\n")
            else:
                break

        contact: Contact = Contact(name, num, addr)
        
        self._contacts.append(contact)
        self._save()

    def _delete(self) -> None:
        print("\nEnter the number of the contact you would like to delete:")
        for index, item in enumerate(self._contacts):
            print(f"\t[{index+1}] {item.name}")
        try:
            index = int(input())-1
            if index <= len(self._contacts):
                self._contacts.pop(index)
                self._save()
            else:
                print("ERROR: Invalid contact number. Please try again...")

        except ValueError:
            print("ERROR: Invalid contact number. Please try again...")

    def _save(self) -> None:
        self._write_file(self.__CONTACTS_DIR, dumps(list(repr(self._contacts[index]) for index, _ in enumerate(self._contacts)), sort_keys=True, indent=4))

    def _load(self) -> list[Contact]:
        for item in self._read_json(self.__CONTACTS_DIR):
            yield eval(item)

    @classmethod
    def _read_json(cls, path: str) -> list or dict:
        return loads(open(path, "r").read()) if Path(path).is_file() else die("ERROR: File '{path}', does not exist...")

    @classmethod
    def _write_file(cls, path: str, data: str) -> None:
        with open(path, "w") as fn:
            fn.write(data)


def run() -> None:
    main: Main = Main()
    main.run()


if __name__ == "__main__":
    run()
