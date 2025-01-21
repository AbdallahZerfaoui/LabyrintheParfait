class memory:
    def __init__(self):

        List = []
        self.state = List

    def is_empty(self):
        if len(self.state) == 0:
            return True
        else:
            return False

    def store_element(self, element):
        self.state.append(element)

    def get_last_state(self):
        if not self.is_empty():
            return self.state[len(self.state) - 1]
        else:
            print("empty list")

    def pop_last_state(self):
        if not self.is_empty:
            self.state.remove(self.get_last_state())
