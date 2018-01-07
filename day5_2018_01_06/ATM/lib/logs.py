# -*- coding:utf-8 -*-
# User:fucong
# Time：
from conf import settings
import logging.config
def logs(log_name):
    logging.config.dictConfig(settings.LOGGING_DIC)  # 导入上面定义的logging配置
    logger = logging.getLogger(log_name)  # 生成一个log实例

