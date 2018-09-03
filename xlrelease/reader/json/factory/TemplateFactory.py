from Factory import Factory
from ....Template import Template


class TemplateFactory(Factory):

    @staticmethod
    def create(data):
        type = data['type']
        if type == 'xlrelease.Release':
            return Template(data['title'])
        else:
            Factory.raise_exception(type)
