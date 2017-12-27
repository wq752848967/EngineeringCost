# cong:utf-8
# @Author: wangqi
# @Date:    下午11:47
# @Last Modified by:   wangqi
# @Last Modified time:  下午11:47
import leancloud
from datetime import datetime

def testSchemaInit(content):
    log_test = leancloud.Object.extend('log_test')
    log = log_test()
    log.set('content', content)
    log.save()

