class Gun:

    def __init__(self, model):

        # 1.抢的型号
        self.model = model

        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullt(self, count):

        self.bullet_count += count

