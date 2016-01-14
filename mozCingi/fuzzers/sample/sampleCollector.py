__author__ = 'shako'
from mozCingi.steps.collector import AbsCollector
class SampleCollector(AbsCollector):

    def run(self):
        print self.name
        print self.fuzzer_name
        print self.obj_index
        print self.configurations
