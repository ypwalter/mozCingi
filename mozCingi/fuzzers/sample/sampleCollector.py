__author__ = 'shako'
from mozCingi.steps.collector import AbsCollector
class SampleCollector(AbsCollector):

    configurations = {}

    def read_configuration(self, **kwargs):
        self.configurations = kwargs

    def run(self):
        print self.name
        print self.configurations
