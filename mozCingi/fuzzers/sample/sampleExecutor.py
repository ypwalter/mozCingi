__author__ = 'shako'
from mozCingi.steps.executor import AbsExecutor
class SampleExecutor(AbsExecutor):

    def run(self):
        print self.name
        print self.fuzzer_name
        print self.obj_index
        print self.configurations

