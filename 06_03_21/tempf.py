import tempfile
import time
import os
tempfile.tempdir = './..'
f = tempfile.NamedTemporaryFile(suffix='.txt', dir='.', delete=False)
print(tempfile.gettempdir())

f.close()
os.unlink(f.name)

tempdr = tempfile.TemporaryDirectory(prefix='TempDir', suffix='_1', dir='./../..')

f = tempfile.NamedTemporaryFile(suffix='.txt', dir=tempdr.name, delete=False)
time.sleep(30)

tempdr.cleanup()
