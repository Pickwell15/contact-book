class Contact:

    __NAME_DEFAULT: str = "UNKNOWN"
    __NUM_DEFAULT: str = "UNKNOWN"
    __ADDR_DEFAULT: str = "UNKNOWN"

    def __init__(self, name: str, num: str, addr: str) -> None:
        self.name: str = name
        self.num: str = num
        self.addr: str = addr

    def __del__(self) -> None:
        print(f"Contact ({self.name}) deleted... ")

    def __str__(self) -> str:
        return f"NAME: {self.name}" \
            f"NUMBER: {self.num}" \
            f"ADDRESS: {self.addr}"

    def __repr__(self) -> str:
        return f"Contact('{self.name}', '{self.num}', '{self.addr}')"
