__author__ = 'shako'

import gevent
import importlib

class AbsFuzzer(object):

    def __init__(self, name, **kwargs):
        self.name = name
        if "path" in kwargs:
            self.src_conf_path = kwargs['path']
        self.read_configuration(**kwargs)

    def update(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        self.read_configuration(**kwargs)

    def read_configuration(self, **kwargs):
        pass

    def onstop(self):
        pass

    def run(self):
        # create steps, spawn them and wait for them to complete
        steps = ["generator", "executor", "parser", "collector"]
        for step in steps:
            print "Current running steps:: [ %s ]" % step
            running_threads = []
            step_objs = {}
            module_name = ".".join(self.configurations[step]['class_name'].split(".")[:-1])
            class_name = self.configurations[step]['class_name'].split(".")[-1]
            step_module = importlib.import_module(module_name)
            step_class = getattr(step_module, class_name)
            for obj_num in xrange(int(self.configurations[step]['gen_num'])):
                step_class_name = class_name + "_" + str(obj_num)
                step_objs[obj_num] = step_class(step_class_name, self.name, obj_num, **self.configurations[step]['conf'])
                running_threads.append(gevent.spawn(step_objs[obj_num].run))
            gevent.joinall(running_threads)

    def teardown(self):
        pass
