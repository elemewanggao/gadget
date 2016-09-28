# -*- coding:utf-8 -*-
u"""用于UTF-8编码的csv文件能够用EXCEL打开!"""
import csv
import sys
import os


def read_csv(csv_file):
    u"""读取csv文件内容."""
    csv_contents = []
    with open(csv_file, 'rb') as read_csv:
        csv_reader = csv.reader(read_csv)
        for line in csv_reader:
            csv_contents.append(line)
    return csv_contents


def contents_convert(contents):
    u"""Excel对于数字类型如果位数大于11位，会展示为科学计算法方式。如果超过15位，会将后面几位置为0.
    这边做一个转换如果整型位数超过11位，加一个tab标志.
    """
    new_contents = []
    for line in contents:
        new_line = []
        for cell in line:
            cell = cell.strip()
            if str(cell).isdigit() and len(cell) > 11:
                cell = '\t{}'.format(cell)
            new_line.append(cell)
        new_contents.append(new_line)
    return new_contents


def write_csv(csv_file, contents):
    u"""将contents中内容写入csv文件中,在文件头加上\xef\xbb\xbf."""
    new_contents = contents_convert(contents)
    with open(csv_file, 'wb') as write_csv:
        write_csv.write("\xef\xbb\xbf")
        csv_writer = csv.writer(write_csv)
        csv_writer.writerows(new_contents)


def get_new_file_path(csv_file_path, new_file_name=None):
    u"""重命名csv文件."""
    file_dir = os.path.normpath(os.path.dirname(csv_file_path))
    old_file_name = os.path.basename(csv_file_path)
    if not new_file_name:
        new_file_name = old_file_name.split('.')[0] + '_new.csv'
    new_file_path = os.path.join(file_dir, new_file_name)
    return new_file_path


if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise Exception('请输入csv文件或所在目录路径!')
    path_num = len(sys.argv)

    for i in range(1, path_num):
        csv_file_path = sys.argv[i]
        if not os.path.exists(csv_file_path):
            raise Exception('不存在此文件或目录!')
        if os.path.isfile(csv_file_path):
            contents = read_csv(csv_file_path)
            new_file_path = get_new_file_path(csv_file_path)
            write_csv(new_file_path, contents)
        elif os.path.isdir(csv_file_path):
            csv_file_path = os.path.normpath(csv_file_path)
            for dirpath, dirnames, filenames in os.walk(csv_file_path):
                for filename in filenames:
                    if not str(filename).endswith('csv'):
                        continue
                    old_file_path = os.path.join(dirpath, filename)
                    new_file_path = get_new_file_path(old_file_path)
                    contents = read_csv(old_file_path)
                    write_csv(new_file_path, contents)

