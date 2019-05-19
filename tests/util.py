import os
import tempfile
import shutil
from contextlib import contextmanager

@contextmanager
def tmpd():
    cwd0 = os.getcwd()
    tmpd = tempfile.mkdtemp()
    os.chdir(tmpd)

    yield tmpd

    os.chdir(cwd0)
    shutil.rmtree(tmpd)



@contextmanager
def env_context():
    initial_env = os.environ.copy()

    yield

    for var in os.environ.keys():
        if not var in initial_env:
            del os.environ[var]

    for (var,value) in initial_env.items():
        os.environ[var] = value



