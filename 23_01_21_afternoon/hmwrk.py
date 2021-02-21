"""
DEBUG-10
INFO-20
WARNING-30
ERROR-40
CRITICAL-50
"""
import logging
import os
logging.basicConfig(level=logging.ERROR, format='%(asctime)s -- %(levelname)s -- %(name)s -- %(message)s',
                    filename=os.path.normpath('./logs/test.log'))

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')
file_handler = logging.FileHandler(filename=os.path.normpath('./logs/test_2.log'))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def my_func(a, b, c):
    try:
        value = a * b / c
    except ZeroDivisionError as e:
        logger.exception(f'c should not be 0')
    else:
        logger.info(f'Value of my func {value}')
        return value

my_func(1, 3, 4)
my_func(1, 3, 0)

