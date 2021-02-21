from main import division
import unittest

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(1, 1), 1, 'Should be 1')
        self.assertEqual(division(0, 1), 0, 'Should be 0')
        self.assertEqual(division(1, 2), 0.5, 'Should be 0.5')
        # with self.assertRaises(ZeroDivisionError):
        #     division(1, 0)

        # self.assertRaises(ZeroDivisionError, division, 1, 0)

if __name__ == '__main__':
    test_obj = TestDivision()
    print(test_obj.__dict__)
    test_obj.test_division()
    assert division(1, 1) == 1, 'Should be 1'
    # assert division(0, 1) == 0, 'Should be 0'
    # assert division(1, 2) == 0.5, 'Should be 0.5'
    #
    # error_message = ''
    # try:
    #     division(0, 0)
    # except Exception as e:
    #     error_message = str(e)
    # assert error_message == 'division by zero', 'Should be raise division error'