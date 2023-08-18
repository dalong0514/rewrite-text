# -*- coding:utf-8 -*-

import glob, os, time

def write_file():

    # 获取当前文件夹的路径
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # 定义源文件和目标文件的路径
    origin_path = os.path.join(current_directory, 'origin_text.md')
    target_path = os.path.join(current_directory, 'target_text.md')

    # 读取源文件的内容
    with open(origin_path, 'r') as origin_file:
        content = origin_file.read()

    # 将读取的内容写入目标文件
    with open(target_path, 'w') as target_file:
        target_file.write(content)

    print(content)


if __name__ == '__main__':
    start_time = time.time()
    write_file()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
