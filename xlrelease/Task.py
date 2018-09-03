from Variable import set_variable


class Task(object):

    def __init__(self, title):
        self.title = title
        self.precondition = None
        self.subtasks = []
        self._is_executed = False
        self._return_variables = {}

    def get_title(self):
        return self.title

    def add_subtask(self, task):
        self.subtasks.append(task)

    def set_precondition(self, condition):
        self.precondition = condition

    def execute(self, variables):
        if not self.precondition or self.precondition.evaluate(variables):
            if not self.subtasks:
                self._is_executed = True
                for key, value in self._return_variables.items():
                    set_variable(key, value, variables)
            else:
                tmp = False
                for sub in self.subtasks:
                    sub.execute(variables)
                    if sub.is_executed():
                        tmp = True
                self._is_executed = tmp
        else:
            self._is_executed = False

    def is_executed(self):
        return self._is_executed

    def find_task(self, title):
        if title == self.title:
            return self
        for task in self.subtasks:
            tmp = task.find_task(title)
            if tmp:
                return tmp
        return None

    def return_variable(self, key, value):
        self._return_variables[key] = value

    def return_variables(self, dict_of_vars):
        for key, value in dict_of_vars.items():
            self._return_variables[key] = value
