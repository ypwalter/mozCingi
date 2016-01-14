__author__ = 'shako'

from mozCingi.fuzzers.fuzzer import AbsFuzzer
class SampleFuzzer(AbsFuzzer):

    configurations = {}

    def read_configuration(self, **kwargs):
        self.configurations = kwargs
        print self.configurations

