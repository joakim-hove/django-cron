import json
import os
import unittest

from .util import *
from django_cron import Cron

if "DJANGO_SETTINGS_MODULE" in os.environ:
    del os.environ["DJANGO_SETTINGS_MODULE"]


class InitTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_init_path(self):
        with env_context():
            with self.assertRaises(Exception):
                Cron("project", "/does/not/exist")

            with self.assertRaises(Exception):
                Cron("project", "/does/not/exist")

            with tmpd():
                os.makedirs("project/project")

                with open("project/manage.py","w") as f:
                    pass

                with open("project/project/settings.py", "w") as f:
                    pass

                Cron("project", "project")
                self.assertIn("DJANGO_SETTINGS_MODULE", os.environ)

            with tmpd():
                os.makedirs("project")
                with self.assertRaises(Exception):
                    Cron("project", "project")

        self.assertNotIn("DJANGO_SETTINGS_MODULE", os.environ)


    def test_init_env(self):
        with env_context():
            with tmpd():
                os.makedirs("project/project")

                with open("project/manage.py","w") as f:
                    pass

                with open("project/project/settings.py", "w") as f:
                    pass

                d = {"VAR1" : "Value1",
                     "VAR2" : "Value2"}

                with open("project/settings.json", "w") as f:
                    f.write(json.dumps(d))

                Cron("project", "project")
                self.assertEqual(os.environ["VAR1"], "Value1")
                self.assertEqual(os.environ["VAR2"], "Value2")


    def test_run(self):
        with env_context():
            with tmpd():
                os.makedirs("project/project")

                with open("project/manage.py","w") as f:
                    pass

                with open("project/project/settings.py", "w") as f:
                    pass

                cron = Cron("project", "project")
                with self.assertRaises(IOError):
                    cron.run(["does/not/exist"])





if __name__ == "__main__":
    unittest.main()
