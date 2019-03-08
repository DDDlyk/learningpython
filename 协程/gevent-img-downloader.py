import urllib.request
import gevent
from  gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "3.jpg", "https://rpic.douyucdn.cn/live-cover/roomCover/2019/01/30/83427d6b868ca797acdbf23ed4860d2f_big.jpg"),
        gevent.spawn(downloader, "4.jpg", "https://rpic.douyucdn.cn/live-cover/appCovers/2019/02/28/6440485_20190228191740_small.jpg"),
    ])


if __name__ == '__main__':
    main()
