


KeyError
SyntaxError
IndentationError
TypeError

#StopIteration
def stopIteration():
    arr = [1]
    iter = arr.__iter__()
    print(iter.__next__())
    print(iter.__next__())

#ZeroDivisionError
def zeroException():
    print(5/0)

#AssertionError
def asserterror():
    x = 1
    assert x == 0
    print("all good")
#ImportError
def importerr():
    from hi import fakemodule
    print("import success")
#zeroException()
#stopIteration()
#asserterror()
#importerr()