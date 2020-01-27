import json
import os
import os.path
import subprocess

class Cron(object):
    def __init__(self, project, project_root):
        self.project = project
        self.project_root = project_root

        if not os.path.isdir(self.project_root):
            raise Exception("The directory: {} does not exist".format(self.roject_root))

        self.manage_script = os.path.join(self.project_root, "manage.py")
        if not os.path.isfile(self.manage_script):
            raise Exception("Can not find manage script: {}".format(self.manage_script))

        settings_file = os.path.join(self.project_root, self.project, "settings.py")
        settings_package = os.path.join(self.project_root, self.project, "settings", "__init__.py")

        if not (os.path.isfile(settings_file) or os.path.isfile(settings_package)):
            raise Exception("Could not find django settings {} or {}".format(settings_file, settings_package))

        settings_module = "{}.settings".format(self.project)
        settings_json = os.path.join( self.project_root, "settings.json")


        if os.path.isfile(settings_json):
            with open(settings_json) as fileH:
                env_settings = json.loads( fileH.read() )

            for var,value in env_settings.items():
                os.environ[var] = value

        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module



    def run_script(self, cmd_file):
        with open(cmd_file) as f:
            lines = f.readlines()
            if not lines:
                lines = [""]

        for line in lines:
            cmd = os.path.basename( cmd_file )
            argv = line.split()
            cmd_list = [ self.manage_script , cmd ] + argv
            print("Running: {}".format(" ".join(cmd_list)))
            status = subprocess.call( cmd_list )



    def run(self, path_list):
        for path in path_list:
            full_path = os.path.join(self.project_root, path)
            if os.path.isdir(full_path):
                for elm in os.listdir(full_path):
                    self.run_script(os.path.join(full_path, elm))
            elif os.path.isfile(full_path):
                self.run_script(full_path)
            else:
                raise IOError("Argument: {} does not correspond to an existing entry".format(path))
