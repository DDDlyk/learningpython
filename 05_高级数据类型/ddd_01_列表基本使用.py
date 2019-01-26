name_list = ["zhangsan", "lisi", "wangwu"]

# 列表索引超出范围
print(name_list[2])


print(name_list.index("wangwu"))

name_list[1] = "李四"
print(name_list[1])
temp_list = ["孙悟空", "猪二哥", "沙师弟"]

name_list.append("王小二")
name_list.insert(2, "王五")
name_list.extend(temp_list)
name_list.remove("王五")
name_list.pop()
name_list.pop(3)

print(name_list)
