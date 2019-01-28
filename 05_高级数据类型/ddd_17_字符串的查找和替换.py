hello_str = "hello world"

# 1、判断字符串是否以指定字符开始
print(hello_str.startswith("Hello"))

# 2、判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3、查找指定字符串
print(hello_str.find("llo"))
print(hello_str.find("abc"))
# 4、替换字符串
new_str = hello_str.replace("world", "python")
print(new_str)
