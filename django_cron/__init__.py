import json
import os
import os.path


def init(argv):
    project = argv[0]
    project_root = argv[1]

    if not os.path.isdir(project_root):
        raise Exception("The directory: {} does not exist".format(project_root))

    manage_script = os.path.join(project_root, "manage.py")
    if not os.path.isfile(manage_script):
        raise Exception("Can not find manage script: {}".format(manage_script))

    settings_file = os.path.join(project_root, project, "settings.py")
    settings_package = os.path.join(project_root, project, "settings", "__init__.py")

    if not (os.path.isfile(settings_file) or os.path.isfile(settings_package)):
        raise Exception("Could not find django settings {} or {}".format(settings_file, settings_package))

    settings_module = "{}.settings".format(project)
    settings_json = os.path.join( project_root, "settings.json")


    if os.path.isfile(settings_json):
        with open(settings_json) as fileH:
            env_settings = json.loads( fileH.read() )

        for var,value in env_settings.iteritems():
            os.environ[var] = value



    os.environ["DJANGO_SETTINGS_MODULE"] = settings_module
