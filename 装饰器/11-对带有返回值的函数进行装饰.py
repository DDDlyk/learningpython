def set_func(func):
    print("----开始进行装饰---")

    def call_func(*args, **kwargs):
        print("-----这是权限验证1-----")
        print("-----这是权限验证2-----")
        return func(*args, **kwargs)
    return call_func


@set_func
def test1(num, *args, **kwargs):
    print("-----test1-----%d" % num)
    print("-----test1-----", args)
    print("-----test1-----", kwargs)
    return "ok"


@set_func
def test2():
    pass


ret = test1(100)
print(ret)

ret = test2(100)
print(ret)