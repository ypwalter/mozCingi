__author__ = 'shako'
class AbsStep(object):
    def __init__(self, name, **parameters):
        self.name = name
        self.read_configuration(**parameters)

    def read_configuration(self, **parameters):
        pass

    def run(self):
        pass

