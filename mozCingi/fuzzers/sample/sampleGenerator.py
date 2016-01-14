__author__ = 'shako'
from mozCingi.steps.generator import AbsGenerator
class SampleGenerator(AbsGenerator):

    def run(self):
        print self.name
        print self.configurations


