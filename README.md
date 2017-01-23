Obfuscating the test cases is a bit complicated, and requires the TA to follow the following steps.

1. Create operations.py which contains the operations you want to test.
2. Create tests.py which contains the test cases. 
3. Run tests.py. In this example, the output I get is :
======================================================================
FAIL: testMultiply (__main__.FooTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 12, in testMultiply
    assert multiply(4, 5) == 0
AssertionError

======================================================================
FAIL: testSubtract (__main__.FooTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests.py", line 9, in testSubtract
    assert subtract(5, 9) == -5
AssertionError

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=2)
False
[]
[(<__main__.FooTest testMethod=testMultiply>, 'Traceback (most recent call last):\n  File
"tests.py", line 12, in testMultiply\n    assert multiply(4, 5) == 0\nAssertionError\n'),
(<__main__.FooTest testMethod=testSubtract>, 'Traceback (most recent call last):\n  File "
tests.py", line 9, in testSubtract\n    assert subtract(5, 9) == -5\nAssertionError\n')]
[] 

which clearly shows that 2/3 tests have failed. You might want to format this differently. Now, we do not want to provide this exact code to the student, because they will have knowledge of the test cases. 

4. Instead, run : cython tests.py -o tests.c 

Now, the student, who has tests.c has to run the following code on a Mac OS/Linux machine. (Will figure out windows soon)

1. Make sure operations.py is in the same directory directory, and create an empty file also in the same directory called __init__.py
2. export C_INCLUDE_PATH=/System/Library/Frameworks/Python.framework/Headers/ (if mac)

export C_INCLUDE_PATH=/usr/include/python2.7/ (if linux)

3. gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lpython2.7 -o tests.so tests.c
4. this creates tests.so
    - if you get Python.h, no such file or directory, its because your C_INCLUDE_PATH might be wrong. Basically : export the place where you have Python.h, which you need 

5. open up a python or ipython terminal and run : from tests import main
6. The output you get is : 

In [1]: from tests import main
.FF
======================================================================
FAIL: testMultiply (pcode.tests.FooTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "pcode/tests.py", line 12, in pcode.tests.FooTest.testMultiply (tests.c:1196)
  AssertionError

  ======================================================================
  FAIL: testSubtract (pcode.tests.FooTest)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "pcode/tests.py", line 9, in pcode.tests.FooTest.testSubtract (tests.c:1118)
    AssertionError

    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    FAILED (failures=2)
    False
    []
    [(<pcode.tests.FooTest testMethod=testMultiply>, 'Traceback (most recent call last):\n  Fi
    le "pcode/tests.py", line 12, in pcode.tests.FooTest.testMultiply (tests.c:1196)\nAssertio
    nError\n'), (<pcode.tests.FooTest testMethod=testSubtract>, 'Traceback (most recent call l
    ast):\n  File "pcode/tests.py", line 9, in pcode.tests.FooTest.testSubtract (tests.c:1118)
    \nAssertionError\n')]
    []

Which is the same output
7. Thus, the student has executed the test without any access to source.


