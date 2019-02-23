# 1.打开文件
file_read = open("readme")
file_write = open("readme[复件]", "w")

# 2.读、写操作
while True:
    # 读取一行内容
    text = file_read.readline()

    # 判断是否读取到内容
    if not text:
        break
    file_write.write(text)

# 3.关闭文件
file_read.close()
file_write.close()
