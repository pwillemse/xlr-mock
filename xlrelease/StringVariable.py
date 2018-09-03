from Variable import Variable


class StringVariable(Variable):

    def __init__(self, key):
        Variable.__init__(self, key)

    def set_value(self, value):
        if isinstance(value, str):
            value = value.decode('utf8')

        if value == u'null':
            value = None

        if self.is_valid(value, unicode) or value is None:
            self.value = value
        else:
            self.raise_exception()

    def to_string(self):
        if self.value is None:
            return 'None'
        else:
            return "'%s'" % self.value
