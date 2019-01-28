students = [
    {"name": "阿土"},
    {"name": "小美"}
]


find_name = "李四"

for stu_dict in students:

    print(stu_dict)

    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        break

    else:
        print("抱歉没有找到%s" % find_name)
# else:
#     # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
#     # 还希望的到一个统一的提示！
#     print("抱歉没有找到%s" % find_name)
print("循环结束")
