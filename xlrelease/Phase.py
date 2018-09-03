
def find_phase(title, phases):
    for phase in phases:
        if title == phase.get_title():
            return phase
    raise Exception('Phase (%s) not found!' % title)


class Phase(object):

    def __init__(self, title):
        self.title = title
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def get_title(self):
        return self.title

    def execute(self, variables):
        for task in self.tasks:
            task.execute(variables)

    def are_tasks_executed(self):
        for task in self.tasks:
            if task.is_executed():
                return True
        return False

    def find_task(self, title):
        for task in self.tasks:
            tmp = task.find_task(title)
            if tmp:
                return tmp
        return None
