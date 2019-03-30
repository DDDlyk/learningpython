def set_func(func):
    print("----开始进行装饰---")
    def call_func(a):
        print("-----这是权限验证1-----")
        print("-----这是权限验证2-----")
        func(a)
    return call_func


@set_func
def test1(num):
    print("-----test1-----%d" % num)


@set_func
def test2(num):
    print("-----test2-----%d" % num)
#
#
# test1(100)
# test2(200)

