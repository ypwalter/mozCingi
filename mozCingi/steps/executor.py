__author__ = 'shako'
from mozCingi.steps.step import AbsStep
class AbsExecutor(AbsStep):
    pack_file_name = ""
    launch_file_name = ""
    output_dir_path = ""
    tmp_dir_path = ""

    def remove_src_conf(self):
        pass

    def unpack_data(self):
        pass

    def launch_execute_file(self):
        pass

    def launch_parser(self):
        pass

    def launch_collector(self):
        pass

    def run(self):
        self.unpack_data()
        self.launch_execute_file()
        self.launch_parser()
        self.launch_collector()

