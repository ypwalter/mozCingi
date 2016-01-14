__author__ = 'shako'
from mozCingi.steps.parser import AbsParser
class SampleParser(AbsParser):

    def run(self):
        print self.name
        print self.fuzzer_name
        print self.obj_index
        print self.configurations


