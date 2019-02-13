def print_info(name, title="", gender=True):
    """

    :param title: 职位
    :param name: 班上同学的姓名
    :param gender: True男生False女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("[%s]%s 是 %s" % (title, name, gender_text))


# 假设班上男生居多
# 提示：在制定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("老王")
print_info("小明")
print_info("小美", gender=False)
