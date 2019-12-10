import unittest,time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from Sample.packages.HTMLTestRunner import HTMLTestRunner

test_dir = '../case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%M-%D %H_%M_%S")
    filename = 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test report Mini',
                            description='用例执行情况：')
    runner.run(discover)
    fp.close()