def readfile(filename):
    print("__CONTENT_START__")

    try:
        file = open(filename)
        lines = file.readlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("__NO_SUCH_FILE__")
    print("__CONTENT_END__")

readfile('try_catch.py')