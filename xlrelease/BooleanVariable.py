from Variable import Variable


class BooleanVariable(Variable):

    def __init__(self, key):
        Variable.__init__(self, key)

    def set_value(self, value):
        if self.is_valid(value, bool):
            self.value = value
        else:
            self.raise_exception()

    def to_string(self):
        if self.value is None:
            return 'None'
        elif self.value:
            return 'True'
        else:
            return 'False'
