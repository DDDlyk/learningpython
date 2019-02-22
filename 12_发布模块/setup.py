from distutils.core import setup

setup()
setup(name="ddd_message",  # 包名
      version="1.0",  # 版本
      description="ddd's 发送和接受消息模块",  # 描述信息
      author="ddd",  # 作者
      author_email="DDDlyk@qq.com",  # 作者邮箱
      url="dddlyk.com",  # 主页
      py_modules=["ddd_message.send_message",
                  "ddd_message.receive_message"])
