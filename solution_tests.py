###
# Title: Assignment B Solution Unit Tests
# Description: Solution Unit Tests for Assignment B
# Author: Lu Yaomin
#
# History:
# 20210325 - v1.0: Unit test for the two classes in solution
###
import unittest
from solution import Sentosa, Sentosa_bitwise

class SentosaTest(unittest.TestCase):
    def test_sentosa1(self):
        sentosa = Sentosa()
        print('Testing for solution class Sentosa')
        for x in range(1,101):
            sentosa.print_num(x)

    def test_sentosa_bitwise(self):
        sentosa_bitwise = Sentosa_bitwise()
        print('Testing for solution class Sentosa_bitwise')
        for x in range(1,101):
            sentosa_bitwise.print_num(x)

if __name__ == '__main__':
    unittest.main()
