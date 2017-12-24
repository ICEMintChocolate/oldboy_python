# -*- coding:utf-8 -*-
# User:fucong
# Time：
import time
def tail(filepath):
    with open(filepath,'rb') as f:
        f.seek(0,2) #移动到文件末尾
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(0.05)

def grep(lines,pattern):
    for line in lines:
        line = line.decode('utf-8')
        if pattern in line:
            yield line

lines = grep(tail('access.log'),'404')

for line in lines:
    print(line)