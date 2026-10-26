# coding: utf-8

import logging
import os

"""
  等级：
    debug         调试
    info          信息
    warning       警告
    error         错误，业务异常
    critical      严重错误，系统异常

    basicConfig 参数
      level：设置日志级别，低于该级别的日志将被忽略
      format：设置日志输出格式
      filename：设置日志输出文件名及地址，若不设置则输出到控制台
      filemode：设置日志输出文件的模式，默认是'a'，即追加模式 ， w表示覆盖模式


    format参数：
      %(levelno)s：打印日志级别的数值
      %(levelname)s：打印日志级别的名称
      %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
      %(filename)s：打印当前执行程序名
      %(funcName)s：打印日志的当前函数
      %(lineno)d：打印日志的当前行号
      %(asctime)s：打印日志的时间
      %(message)s：打印日志信息

  format示例：
    format=''%(asctime)s - %(pathname)s[line:%(lineno)s] - %(levelname)s: %(message)s'
"""

# basicConfig
""" logging.basicConfig(
  level=logging.DEBUG,
  format='%(asctime)s - %(pathname)s[line:%(lineno)s] - %(levelname)s: %(message)s',
  # 日志文件
  filename='logs/py_log.log',
  # 文件模式
  filemode='a'
)

logging.warning('warning info')
logging.error('error info')
logging.critical('critical info') """

def custom_log(path):
  if os.path.exists(path):
    model = 'a'
  else:
    model = 'w'
  logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(pathname)s[line:%(lineno)s] - %(levelname)s: %(message)s',
    # 日志文件
    filename=path,
    # 文件模式
    filemode=model
  )
  return logging

log = custom_log('logs/py_log.log')
log.warning('warning info')
log.error('error info')