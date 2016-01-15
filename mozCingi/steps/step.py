__author__ = 'shako'
class AbsStep(object):

    DEFAULT_ROOT_DATA_DIR = "data"
    DEFAULT_ROOT_OUTPUT_DIR = "output"
    DEFAULT_ROOT_LOG_DIR = "log"
    DEFAULT_ROOT_TMP_DIR = "tmp"
    DEFAULT_ROOT_LIB_DIR = "lib"

    configurations = {}

    def __init__(self, name, fuzzer_name, obj_index, **parameters):
        self.name = name
        self.fuzzer_name = fuzzer_name
        self.obj_index = obj_index
        self.read_configuration(**parameters)

    def read_configuration(self, **kwargs):
        self.configurations = kwargs

    def run(self):
        pass

