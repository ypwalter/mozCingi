__author__ = 'shako'
from mozCingi.steps.generator import AbsGenerator
class SampleGenerator(AbsGenerator):

    def run(self):
        print self.name
        print self.fuzzer_name
        print self.obj_index
        print self.configurations


