import re
from .Variable import find_variable


class Condition(object):

    def __init__(self, condition, task):
        self.condition = condition
        self.task = task

    def evaluate(self, variables):
        tmp = self.condition
        tmp = self.replace_variables(tmp, variables)
        tmp = self.replace_envars(tmp, variables)
        try:
            # functions below must be handled with care. Usage of eval and exec is not recommended!
            if 'result' in tmp:
                return Condition._execute_statement(tmp)
            else:
                return Condition._evaluate_statement(tmp)
        except:
            raise Exception('Evaluation error in task (%s): %s' % (self.task.get_title(), tmp))

    def replace_variables(self, condition, variables):
        items = re.findall('\[(.*?)\]', condition)
        for item in items:
            key = item.replace("'", '').replace('"', '')
            condition = condition.replace('releaseVariables[%s]' % item, find_variable(key, variables).to_string())
        return condition

    def replace_envars(self, condition, variables):
        vars = re.findall('\{(.*?)\}', condition)
        for var in vars:
            condition = condition.replace('${%s}' % var, find_variable(var, variables).to_string())
        return condition

    @staticmethod
    def _evaluate_statement(statement):
        return eval(statement)

    @staticmethod
    def _execute_statement(statement):
        result = False
        exec(statement)
        return result
