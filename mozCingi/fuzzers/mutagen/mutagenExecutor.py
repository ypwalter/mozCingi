__author__ = 'shako'
import os
from mozCingi.steps.executor import AbsExecutor
class MozITPExecutor(AbsExecutor):
    adb_cmd = "adb"
    devices = {}

    def stop_itp(self):
        cmd_str = "cd MozITP;bash stop.sh"
        os.system(cmd_str)

    def launch_execute_file(self):
        pack_file_path = os.path.join(self.DEFAULT_ROOT_TMP_DIR, self.pack_file_name)
        execution_log_dir = os.path.join(self.DEFAULT_ROOT_LOG_DIR, self.__class__.__name__)
        if os.path.exists(execution_log_dir) is False:
            os.makedirs(execution_log_dir)
        execution_log_path = os.path.join(execution_log_dir, self.DEFAULT_EXEC_LOG_NAME)
        cmd_str = "cd MozITP;bash launch.sh fuzz ../%s 2>&1 > ../%s" % (pack_file_path, execution_log_path)
        print "launch_execute_file: %s" % cmd_str
        os.system(cmd_str)
        self.stop_itp()


