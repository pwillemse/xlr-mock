
def find_variable(key, variables):
    for var in variables:
        if key == var.get_key():
            return var
    raise Exception('Variable (%s) not found!' % key)


def get_variable(key, variables):
    var = find_variable(key, variables)
    return var.get_value()


def set_variable(key, value, variables):
    var = find_variable(key, variables)
    var.set_value(value)


class Variable(object):

    def __init__(self, key):
        self.key = key
        self.value = None

    def get_key(self):
        return self.key

    def is_valid(self, value, type):
        return isinstance(value, type)

    def get_value(self):
        return self.value

    def set_value(self, value):
        raise Exception('Implementation required!')

    def to_string(self):
        raise Exception('Implementation required!')

    def raise_exception(self):
        raise Exception('Variable with key (%s) has an invalid value!' % self.key)
