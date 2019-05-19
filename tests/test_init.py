import yaml
import os
import unittest

from .util import *
from django_cron import init


class InitTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_init_path(self):
        if "DJANGO_SETTINGS_MODULE" in os.environ:
            del os.environ["DJANGO_SETTINGS_MODULE"]

        with env_context():
            with self.assertRaises(Exception):
                init([])

            with self.assertRaises(Exception):
                init(["project", "/does/not/exist"])

            with self.assertRaises(Exception):
                init(["project", "/does/not/exist"])

            with tmpd():
                os.makedirs("project/project")

                with open("project/manage.py","w") as f:
                    pass

                with open("project/project/settings.py", "w") as f:
                    pass

                init(["project", "project"])
                self.assertIn("DJANGO_SETTINGS_MODULE", os.environ)

                init(["sleipner", "/home/hove/sleipner/sleipner"])
            with tmpd():
                os.makedirs("project")
                with self.assertRaises(Exception):
                    init(["project", "project"])

        self.assertNotIn("DJANGO_SETTINGS_MODULE", os.environ)


if __name__ == "__main__":
    unittest.main()
