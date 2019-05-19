import json
import os
import os.path

class Cron(object):
    def __init__(self, argv):
        self.project = argv[0]
        self.project_root = argv[1]

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

            for var,value in env_settings.iteritems():
                os.environ[var] = value

        os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
