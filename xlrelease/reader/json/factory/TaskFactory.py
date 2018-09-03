from Factory import Factory
from ....Condition import Condition
from ....Task import Task


class TaskFactory(Factory):

    types = [
        'xlrelease.CustomScriptTask',
        'xlrelease.ScriptTask',
        'xlrelease.SequentialGroup'
    ]

    @staticmethod
    def create(data):
        type = data['type']
        if type in TaskFactory.types:
            task = Task(data['title'])
        else:
            Factory.raise_exception(type)

        if 'precondition' in data.keys():
            task.set_precondition(Condition(data['precondition'], task))

        return task
