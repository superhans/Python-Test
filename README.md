# TA side

Obfuscating the test cases is a bit complicated, and requires the TA to follow the following steps.

1. Create ```operations.py``` which contains the methods you want to test.
2. Create ```tests.py``` which contains the test cases. Remember that ```tests.py``` begins with ```# cython: emit_code_comments=False``` so that comments aren't included. (Otherwise the native python code would be included as a comment in the C Code)
3. Run ```tests.py```. In this example, the output I get is :

```
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
```
which clearly shows that 2/3 tests have failed. You might want to format this differently. Now, we do not want to provide this exact code to the student, because they will have knowledge of the test cases. 

4. Instead, run : ```cython tests.py -o tests.c ```

# Student side

Now, the student, who has ```tests.c``` has to run the following code on a Mac OS/Linux machine. (Will figure out windows soon)

1. Make sure ```operations.py``` is in the same directory directory, and create an empty file also in the same directory called ```__init__.py```
2. Next, run :

```export C_INCLUDE_PATH=/System/Library/Frameworks/Python.framework/Headers/``` (if mac)

```export C_INCLUDE_PATH=/usr/include/python2.7/``` (if linux)

3. Now, run ```gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lpython2.7 -o tests.so tests.c```
4. this creates ```tests.so```
    - if you get an error : ```Python.h, no such file or directory```, its because your ```C_INCLUDE_PATH``` might be wrong. In short : ```export``` the folder which contains ```Python.h```, which you need for compilation. 

5. open up a python or ipython terminal and run : ```from tests import main```
6. The output you get is : 

```
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
```
Which is the same output as the TA side. Remember : you only need to do the compilation once. Just run ```from tests import main``` whenever you would like to test. 

7. Thus, the student has executed the test without any access to source code of test.


