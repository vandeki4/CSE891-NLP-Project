import unittest
from ..scripts.utility import *
import os

class MyTestCase(unittest.TestCase):
    def test_pair_wise_1(self):
        file1 = 'this sentence from file1\nsentence2file1'
        file2 = 'this sentence from file2\nsentence2file2'
        with open('test1.txt', 'w') as f1:
            f1.write(file1)
        with open('test2.txt', 'w') as f2:
            f2.write(file2)

        self.assertEqual([('this sentence from file1', 'this sentence from file2'),
                            ('sentence2file1', 'sentence2file2')], pair_wise('test1.txt', 'test2.txt'))
        os.remove('test1.txt')
        os.remove('test2.txt')


if __name__ == '__main__':
    unittest.main()
