import unittest
from black_jack_2.tests import TestCard


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCard())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
