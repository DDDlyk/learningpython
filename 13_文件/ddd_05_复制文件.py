# 1.打开文件
file_read = open("readme")
file_write = open("readme[复件]", "w")

# 2.读、写操作
text = file_read.read()
file_write.write(text)

# 3.关闭文件
file_read.close()
file_write.close()
