__author__ = 'shako'
class AbsStep(object):

    configurations = {}

    def __init__(self, name, **parameters):
        self.name = name
        self.read_configuration(**parameters)

    def read_configuration(self, **kwargs):
        self.configurations = kwargs

    def run(self):
        pass

