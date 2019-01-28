space_str = "   \t\n\r"

print(space_str.isspace())

# 2、判断字符串中包含数字
# num_str = "1.1"
# Unicode字符串
num_str = "\u00b2"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())

