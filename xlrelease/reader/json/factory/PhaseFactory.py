from Factory import Factory
from ....Phase import Phase


class PhaseFactory(Factory):

    @staticmethod
    def create(data):
        type = data['type']
        if type == 'xlrelease.Phase':
            return Phase(data['title'])
        else:
            Factory.raise_exception(type)
