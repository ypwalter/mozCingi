__author__ = 'shako'
from mozCingi.steps.executor import AbsExecutor
class SampleExecutor(AbsExecutor):

    def run(self):
        print self.name
        print self.configurations

