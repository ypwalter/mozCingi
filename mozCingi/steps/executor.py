__author__ = 'shako'
from mozCingi.steps.step import AbsStep
class AbsExecutor(AbsStep):

    def unpack_data(self):
        pass

    def launch_execute_file(self):
        pass

    def run(self):
        self.unpack_data()
        self.launch_execute_file()

