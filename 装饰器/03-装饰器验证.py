import time


def set_func(func):
    def call_func():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("all time is %f" % (stop_time-start_time))
    return call_func


@set_func
def test1():
    print("-----test1-----")
    for i in range(100000):
        pass

# ret = set_func(test1)
# ret()

# test1 = set_func(test1)
test1()

# test1()
