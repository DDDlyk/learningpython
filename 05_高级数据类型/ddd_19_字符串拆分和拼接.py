# 假设：以下内容是从网络上抓取的
# 要求
# 1.将字符串中的空白字符全部去掉
# 2.再使用“ ”座位分隔符，拼接成一个整齐的字符串

poem_str = "登鹳雀楼 \t 王之涣 \t 白日依山尽 \t \n 黄河入海流 \t \n 欲穷千里目 \t \t 更上一层楼"

print(poem_str)

poem_list = poem_str.split()
print(poem_list)
result = " ".join(poem_list)
print(result)
