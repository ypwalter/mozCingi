__author__ = 'shako'
from mozCingi.steps.step import AbsStep
class AbsParser(AbsStep):

    def output_data(self):
        pass

    def parse_data(self):
        pass

    def run(self):
        self.parse_data()
        self.output_data()

