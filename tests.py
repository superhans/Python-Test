# cython: emit_code_comments=False
from operations import add, subtract, multiply
import unittest

class FooTest(unittest.TestCase):
    def testAdd(self):
        assert add(3, 4) == 7

    def testSubtract(self):
        assert subtract(5, 9) == -5

    def testMultiply(self):
        assert multiply(4, 5) == 0

def main():
    fooSuite = unittest.TestLoader().loadTestsFromTestCase(FooTest)
    fooRunner = unittest.TextTestRunner()
    fooResult = fooRunner.run(fooSuite)
    
    print fooResult.wasSuccessful()
    print fooResult.errors
    print fooResult.failures
    print fooResult.skipped

main()
