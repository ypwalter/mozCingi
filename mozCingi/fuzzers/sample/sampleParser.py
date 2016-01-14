__author__ = 'shako'
from mozCingi.steps.parser import AbsParser
class SampleParser(AbsParser):

    def run(self):
        print self.name
        print self.configurations


