import copy
from Phase import find_phase
from Variable import set_variable


class Release(object):

    def __init__(self, template):
        self.template = copy.deepcopy(template)

    def execute(self):
        for phase in self.template.get_phases():
            phase.execute(self.template.variables)

    def set_variable(self, key, value):
        set_variable(key, value, self.template.get_variables())

    def are_tasks_executed_in_phase(self, title):
        phase = find_phase(title, self.template.get_phases())
        return phase.are_tasks_executed()

    def is_task_executed(self, title):
        task = self.find_task(title)
        return task.is_executed()

    def find_task(self, title):
        for phase in self.template.get_phases():
            task = phase.find_task(title)
            if task:
                return task
        raise Exception('Task (%s) not found!' % title)

    def get_phases(self):
        return self.template.get_phases()
