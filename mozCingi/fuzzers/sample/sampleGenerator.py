__author__ = 'shako'
from mozCingi.steps.generator import AbsGenerator
class SampleGenerator(AbsGenerator):

    configurations = {}

    def read_configuration(self, **kwargs):
        self.configurations = kwargs

    def run(self):
        print self.name
        print self.configurations


