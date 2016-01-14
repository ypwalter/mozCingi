__author__ = 'shako'
from mozCingi.steps.step import AbsStep
class AbsGenerator(AbsStep):

    def generate_data(self):
        pass

    def generate_steps(self):
        pass

    def generate_execution_file(self):
        pass

    def pack_files(self):
        pass

    def generate_conf_file(self):
        pass

    def run(self):
        self.generate_data()
        self.generate_steps()
        self.generate_execution_file()
        self.pack_files()
        self.generate_conf_file()


