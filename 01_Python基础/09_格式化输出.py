# 定义字符串name，输出 我的名字叫 小明，请多多关照！
name = "大小明"
print("我的名字叫 %s，请多多关照！"%name)

# 定义整数变量 student_no，输出 我的学号是000001
student_no = 100123456
print("我的学号是 %06d"%student_no)

# 定义小数price、weight、money
# 输出苹果单价 9.00元/斤，购买了 5.00斤，需支付45元
price = 8.5
weight = 7.5
money = price * weight
print("苹果单价 %.2f元 /斤，购买 %.3f 了斤，需要支付 %.4f 元"%(price, weight, money))

# 定义一个小数scale，输出 数据比例是 10.00%
scale = 0.25
print("数据比例是 %.2f%%" % (scale * 100))

