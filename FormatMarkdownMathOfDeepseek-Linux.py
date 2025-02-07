import os
import re
import sys


def replace_text(content):
    # 替换所有的 ‘\( ’ ‘ \)’ 为 ‘$’
    content = re.sub(r'\\\( ', r"$\\displaystyle ", content)
    content = re.sub(r' \\\)', '$', content)
    # 替换所有的 ‘\( ’ ‘ \)’ 为 ‘$’
    content = re.sub(r'\\\(', r"$\\displaystyle ", content)
    content = re.sub(r'\\\)', '$', content)

    # 替换所有的 ‘\([’ ‘]\)’ 为 ‘$[’ ‘]$’
    content = re.sub(r'\\\(\[', '$[', content)
    content = re.sub(r'\]\\\)', ']$', content)

    # # 替换所有的 ‘\[\n’ ‘\n\]’ 为 ‘$$\n’ 和 ‘\n$$’
    # content = re.sub(r'\\\[\n', '$$\n', content)
    # content = re.sub(r'\n\\\]', '\n$$', content)

    # 替换所有的 ‘\[’ ‘\]’ 为 ‘$$’ 和 ‘$$’
    content = re.sub(r'\\\[', '$$', content)
    content = re.sub(r'\\\]', '$$', content)

    return content


def select_file_with_fzf():
    """
    使用 fzf 选择文件
    """
    try:
        # 列出当前目录下的所有文件，并使用 fzf 选择
        file_path = os.popen('find . -type f | fzf').read().strip()
        if not file_path:
            print("未选择文件。")
            sys.exit(1)
        return file_path
    except Exception as e:
        print(f"选择文件时出错: {e}")
        sys.exit(1)


def main():
    # 检查是否通过命令行参数指定了文件路径
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # 如果没有指定文件路径，则使用 fzf 选择文件
        print("未提供文件路径，使用 fzf 选择文件...")
        file_path = select_file_with_fzf()

    # 读取文件内容
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # 替换文本
            new_content = replace_text(content)
            # 输出替换后的内容
            print("替换后的内容：")
            print(new_content)
            # 可以选择将替换后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"文件 {file_path} 已更新。")
    except FileNotFoundError:
        print(f"文件 {file_path} 不存在。")
    except Exception as e:
        print(f"处理文件时出错: {e}")


if __name__ == "__main__":
    main()
