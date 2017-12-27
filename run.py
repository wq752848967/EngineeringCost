# coding:utf-8
from app import app
import leancloud

leancloud.init("5BOAmAw7gmjMBXOMupn9gUAS-gzGzoHsz", "STawKe5Dvy0AyQDOm97o3P9Y")

if __name__ == '__main__':
    app.run(port=8099)