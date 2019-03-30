from pymysql import *


class JD(object):
    def __init__(self):
        # 创建connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='123456',
                       database='jing_dong', charset='utf8')
        # 获得cursor对象
        self.cs1 = self.conn.cursor()

    def __del__(self):
        # 关闭cursor对象
        self.cs1.close()
        self.conn.close()

    def execute(self, sql):
        self.cs1.execute(sql)
        for temp in self.cs1.fetchall():
            print(temp)

    def show_all_items(self):
        """显示所有商品"""
        sql = "select * from goods;"
        self.execute(sql)

    def show_all_cates(self):
        """显示所有分类"""
        sql = "select name from goods_cates;"
        self.execute(sql)

    def show_brands(self):
        """显示所有品牌"""
        sql = "select name from goods_brands;"
        self.execute(sql)

    def add_brands(self):
        item_name = input("请输入新商品分类名称；")
        sql = """insert into goods_cates (name) value ("%s")""" % item_name
        self.execute(sql)
        self.conn.commit()

    @staticmethod
    def print_menu():
        print("------京东商城-----")
        print("1:所有的商品")
        print("2:所有的商品分类")
        print("3:所有的商品品牌分类")
        print("4:添加一个商品分类")
        return input("请输入功能对应的序号")

    def run(self):
        while True:
            op = self.print_menu()
            if op == "1":
                # 查询所有商品
                self.show_all_items()
            elif op == "2":
                # 查询分类
                self.show_all_cates()
            elif op == "3":
                # 查询品牌
                self.show_brands()
            elif op == "4":
                # 添加商评分类
                self.add_brands()
            else:
                print("输入有误，重新输入")


def main():
    # 1.创建一个京东商城对象
    jd = JD()
    # 2.调用这个对象的run方法，让其运行
    jd.run()
    conn = connect(host='localhost', port=3306, user='root', password='123456',
                   database='jing_dong',charset='utf8')


if __name__ == '__main__':
    main()
