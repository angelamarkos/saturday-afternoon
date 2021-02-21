import time
from functools import wraps

def execution_time(f):
    @wraps(f)
    def wrap_f(*args, **kwargs):
        print(f'Start execution of {f.__name__}')
        start_time = time.time()
        value = f(*args, **kwargs)
        end_time = time.time()
        print(f'Function {f.__name__} executed {end_time - start_time} sec.')
        return value


    return wrap_f


def class_time_execution(cls):
    class NewCls(cls):
        def __init__(self, *args, **kwargs):
            self.instanc = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                attr = super(NewCls, self).__getattribute__(item)
            except Exception as e:
                attr = self.instanc.__getattribute__(item)
            if not callable(attr):
                return attr

            return execution_time(attr)

    return NewCls

@class_time_execution
class Test:
    CLASS_ATTR = 'text'
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_a_b(self):
        return self.a + self.b

    def sub_b_c(self):
        return self.b - self.c

    def div_a_c(self):
        return self.a / self.c


test1 = Test(1, 2, 4)
print(test1.add_a_b)
print(Test.CLASS_ATTR)
print(Test.__name__)


