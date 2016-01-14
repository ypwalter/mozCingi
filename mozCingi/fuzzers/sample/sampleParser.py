__author__ = 'shako'
from mozCingi.steps.parser import AbsParser
class SampleParser(AbsParser):

    configurations = {}

    def read_configuration(self, **kwargs):
        self.configurations = kwargs

    def run(self):
        print self.name
        print self.configurations


