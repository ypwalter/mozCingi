__author__ = 'shako'
from mozCingi.steps.executor import AbsExecutor
class SampleExecutor(AbsExecutor):

    configurations = {}

    def read_configuration(self, **kwargs):
        self.configurations = kwargs

    def run(self):
        print self.name
        print self.configurations

