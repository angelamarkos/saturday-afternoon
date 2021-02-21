import threading
import time
import sys
import datetime

global stop
stop = False

class MyThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def stop(self):
        self._is_stopped = True

def func_thread(a, b):
    print('Start of function func_thread')
    time.sleep(5)
    print(a + b)
    print('End of function func_thread')


def func_to_finish():

    print('Starts func_to_finish')
    thread = MyThread(target=func_thread, args=(1, 5))
    thread.start()
    exit = input('Input exit: ')
    if exit:
        sys.exit()
    print('End of func_to_finish')

    return 123

FILE_NAME = 'test_file.txt'
def file_processing():
    print(f'Start file processing at {datetime.datetime.now()}')
    time.sleep(8)
    with open(FILE_NAME, 'w') as f:
        f.write('Text')
    print(f'End file processing at {datetime.datetime.now()}')


if __name__ == '__main__':
    func_to_finish()
    # file_thread = threading.Thread(target=file_processing)
    # file_thread.start()
    # input_string = input('Input string: ')
    # file_thread.join()
    # with open(FILE_NAME, 'r') as f:
    #     print(f.readline())

