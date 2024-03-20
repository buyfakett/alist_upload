# -*- coding: utf-8 -*-            
# @Author : buyfakett
# @Time : 2024/3/20 17:09
import logging
from alist import AList
import sys
from yaml_util import read_yaml

alist_url = str(read_yaml('alist_url', 'config'))
username = str(read_yaml('username', 'config'))
password = str(read_yaml('password', 'config'))

# 日志记录器
logger = logging.getLogger()

# 设置日志级别，只有大于等于这个级别的日志才能输出
logger.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter(
    "[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]    %(message)s"
)

# 输出到控制台
to_console = logging.StreamHandler()
to_console.setFormatter(formatter)
logger.addHandler(to_console)

if len(sys.argv) != 3:
    print('传参数量不对')
    exit(1)
else:
    local_file = sys.argv[1]
    remote_url = sys.argv[2]
    # 初始化 AList3SDK 客户端
    client = AList(alist_url)
    # 登录 AList 服务
    client.login(username, password)
    upload_status = client.upload(remote_url, local_file)
    if upload_status:
        logging.info(f'上传成功，查看地址：{alist_url}{remote_url}')
        logging.info(f'上传成功，下载地址：{alist_url}/d{remote_url}')
    else:
        logging.error('上传失败！！！')
