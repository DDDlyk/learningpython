def print_line(char, times):

    print(char * times)


def print_lines(nums, char, times):
    """打印多行分隔线

    :param nums: 分割线行数
    :param char:分割线字符
    :param times:分割线字符重复次数
    """
    row = 0
    while row < nums:

        print_line(char, times)
        row += 1


print_lines(5, "*", 50)


