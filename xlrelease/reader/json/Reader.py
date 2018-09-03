import json
# import yaml
from factory.PhaseFactory import PhaseFactory
from factory.TemplateFactory import TemplateFactory
from factory.TaskFactory import TaskFactory
from factory.VariableFactory import VariableFactory
from ..Reader import Reader as IReader


class Reader(IReader):

    @staticmethod
    def read_from_file(path):
        with open(path) as f:
            data = json.load(f, encoding='utf8')
            # data = yaml.safe_load(f)
            template = TemplateFactory.create(data)
            for variable in data['variables']:
                template.add_variable(VariableFactory.create(variable))

            for phase in data['phases']:
                created_phase = PhaseFactory.create(phase)
                template.add_phase(created_phase)

                for task in phase['tasks']:
                    created_task = TaskFactory.create(task)
                    created_phase.add_task(created_task)

                    Reader.iterate_subtasks(created_task, task)
        return template

    @staticmethod
    def iterate_subtasks(object, data):
        if 'tasks' in data.keys():
            for task in data['tasks']:
                subtask = TaskFactory.create(task)
                object.add_subtask(subtask)
                Reader.iterate_subtasks(subtask, task)
