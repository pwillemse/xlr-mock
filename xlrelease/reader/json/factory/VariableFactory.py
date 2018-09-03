from Factory import Factory
from ....BooleanVariable import BooleanVariable
from ....StringVariable import StringVariable


class VariableFactory(Factory):

    @staticmethod
    def create(data):
        key = data['key']
        type = data['type']

        if type == 'xlrelease.StringVariable':
            var = StringVariable(key)
        elif type == 'xlrelease.BooleanVariable':
            var = BooleanVariable(key)
        else:
            Factory.raise_exception(type)

        if 'value' in data.keys():
            var.set_value(data['value'])

        return var
