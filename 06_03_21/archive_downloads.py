from urllib import request
import tempfile
import shutil
import mimetypes
import os
import time
import contextlib


endpoints = ['https://www.coolfreecv.com/doc/coolfreecv_resume_en_06_n.docx',
'https://i.pinimg.com/236x/f0/66/96/f06696bd1d3ea207ce9a83d60ab87486.jpg']

tempdir = tempfile.TemporaryDirectory(prefix='Temp_', dir='.')
for endpoint in endpoints:
    extension = endpoint.rsplit('.')[-1]
    response = request.urlopen(endpoint)
    # print(mimetypes.guess_extension(response.headers['Content-Type']))
    with tempfile.NamedTemporaryFile(prefix='temp_', suffix=f'.{extension}', delete=False,
                                dir=tempdir.name) as temp_f:
        shutil.copyfileobj(response, temp_f)

shutil.make_archive('downloads', 'zip', tempdir.name)

class DirectoryManager:
    def __init__(self, name):
        self.name = name
        os.mkdir(name)
        self.current_path = os.path.abspath(os.curdir)

    def __enter__(self):
        os.chdir(self.name)
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.current_path)
        shutil.rmtree(self.name)

with DirectoryManager('xxx') as dr:
    with open('test.txt', 'w') as f:
        f.write('test')
    time.sleep(10)

    shutil.make_archive('./test', 'zip', dr)



@contextlib.contextmanager
def change_dir(path):
    current_path = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current_path)

with change_dir('copy_new_dir/archive_2') as d:
    with open('test_1.txt', 'w') as f:
        f.write('Test text')

print(os.getcwd())