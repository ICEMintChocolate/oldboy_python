# -*- coding:utf-8 -*-
# User:fucong
# Time：
from conf import settings
def db_user():

    f = open(settings.DB_PATH, 'r+', encoding='utf-8')
    for i in l:
        lines = ','.join(i)
        f.write(lines)
    f.flush()
    f.close()