class Contact:
    """
    ATTRIBUTES
    ---------------
    PRIVATE | __NAME_DEFAULT : str
    PRIVATE | __NUM_DEFAULT : str
    PRIVATE | __ADDR_DEFAULT : str

    METHODS
    ---------------
    PRIVATE | __init__ -> None
    PRIVATE | __del__ -> None
    PRIVATE | __str__ -> str
    PRIVATE | __repr__ -> str
    """

    __NAME_DEFAULT: str = "UNKNOWN"
    __NUM_DEFAULT: str = "UNKNOWN"
    __ADDR_DEFAULT: str = "UNKNOWN"

    def __init__(self, name: str = __NAME_DEFAULT, num: str = __NUM_DEFAULT, addr: str = __ADDR_DEFAULT) -> None:
        """
        Is ran when an instance of the class is created.
        Initialises 'name', 'num' and 'addr' to become attributes of the class.

        :param str name: The contacts name.
        :param str num: The contacts phone number.
        :param str addr: The contacts address.

        :return: None
        """

        self.name: str = name
        self.num: str = num
        self.addr: str = addr

    def __del__(self) -> None:
        """
        Is ran when an instance of the class is deleted.

        :return: None
        """

        print(f"Contact ({self.name}) deleted... ")

    def __str__(self) -> str:
        """
        Returns information about the class.

        :return: str
        """

        return f"NAME: {self.name}" \
            f"NUMBER: {self.num}" \
            f"ADDRESS: {self.addr}"

    def __repr__(self) -> str:
        """
        Returns the code required to reproduce the class

        :return: str
        """

        return f"Contact('{self.name}', '{self.num}', '{self.addr}')"
