import os
import re
import argparse

def get_max_number_in_filenames():
    # 获取当前目录下的所有文件
    files = os.listdir('.')
    
    # 初始化最大数字为0
    max_number = 0
    
    # 正则表达式匹配文件名格式 P{数字} {汉字}.md
    pattern = re.compile(r'^P(\d+)\s.*\.md$')
    
    for file in files:
        match = pattern.match(file)
        if match:
            # 提取数字并转换为整数
            number = int(match.group(1))
            if number > max_number:
                max_number = number
    
    return max_number

def create_markdown_files(start_number, count=5):
    for i in range(start_number + 1, start_number + 1 + count):
        filename = f'P{i}.md'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'')
        print(f'已创建文件: {filename}')

if __name__ == '__main__':
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description='创建指定数量的Markdown文件')
    parser.add_argument('-n', '--number', type=int, default=5, help='要创建的文件数量，默认为5')
    args = parser.parse_args()

    # 获取最大数字
    max_number = get_max_number_in_filenames()
    
    # 创建文件
    create_markdown_files(max_number, args.number)