name_list = ["zhangsan", "lisi", "wangwu", "wangxiaoer", "lisi"]
num_list = [6, 8, 4, 1, 10]
print(len(name_list))
# num_list.sort()
num_list.sort(reverse=True)
print(num_list)
num_list.reverse()
print(num_list)
count = name_list.count("lisi")
print(count)

name_list.remove("lisi")
print(name_list)
