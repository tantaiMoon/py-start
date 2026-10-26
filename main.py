# coding:utf-8
#!/usr/bin/env python


import os # 导入os模块
import head_comment # 导入头注释
import variables # 导入变量
import keyword

'''
  脚本名就是文件名，不需要单独指定
'''

def main():
    print("这是主函数入口")
    print("版本：", variables.version)
    print("作者：", variables.author)
    print("创建日期：", variables.create_date)
    head_comment.print_head_comment()

# 主函数,入口语法是整个程序的最后末尾，后面最好不要加任何代码
# 入口语句不是必须的，但是为了规范，最好加上
# 冒号后一定是下一行缩进一个tab（四个空格），否则会报错
if __name__ == "__main__":
    main()



