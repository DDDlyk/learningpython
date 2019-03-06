import os


def main():
    # 1.获取用户要copy的文件夹的名字
    old_floader_name = input("请输入要copy的文件夹的名字：")

    # 2.创建一个新的文件夹
    os.mkdir(old_floader_name + "复件")

    # 3.获取文件夹中待copy的文件名字 os.listdir()
    file_names = os.listdir(old_floader_name)
    print(file_names)
    
    # 4.创建进程池
    # 复制原文件夹中的文件，到新文件夹中的文件去


if __name__ == '__main__':
    main()
