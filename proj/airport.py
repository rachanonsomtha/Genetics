class Airport:
    def __init__(self, name: str, flow: list[int], capacity: int):
        self.name = name
        self.flow = flow
        self.capacity = capacity

    def show(self):
        """Function printing python version."""
        print(
            f"Airport name {self.name}\t  Flow : {self.flow}\tCapacity : {self.capacity}"
        )