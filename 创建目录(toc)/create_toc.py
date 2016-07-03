#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 用来创建 TOC(目录) 用的
"""
import string

__author__ = '__L1n__w@tch'


def get_title(data, title_filter):
    """
    读取 md 格式的数据, 分离出其中的合法标题
    :param data: 要处理的数据, 比如 ['\n', '## 题目 1: just print a+b\n', '### 描述\n']
    :param title_filter: 标题过滤器, ("##", ), 比如说只留下 ## 级的标题
    :return: ["## 题目 1: just print a+b"], 保留所有需要的标题
    """
    title_list = list()
    is_code = False
    for each_line in data:
        if each_line.startswith("```"):
            is_code = ~is_code

        # 代码区的 ## 直接过滤掉
        if is_code:
            continue
        for valid_title in title_filter:
            if each_line.startswith(valid_title + " "):
                title_list.append(each_line.strip())
                break
    return title_list


def get_toc_items(a_list):
    """
    将所有标题分离成描述与链接并返回
    :param a_list: ["## 题目 1: aaa", "### 题目 2: bbb"]
    :return: [("题目 1: aaa", "#题目-1-aaa"), ("题目 2: bbb", "#题目-2-bbb")]
    """
    toc_items = list()
    for each in a_list:
        while each[0] == "#":
            # 比如说 "## 题目 1: aaa", 执行完这个 while 之后就变成了 " 题目 1: aaa"
            each = each[1:]
        description = each[1:]  # 去除空格

        # 去除标点符号
        link = str()
        for char in each[1:]:
            # 英文标点符号处理
            if char in string.punctuation:
                continue
            # 中文标点符号处理
            elif 65281 <= ord(char) <= 65374:
                continue
            link += char

        link = link.lower()
        link = link.replace(" ", "-")

        toc_items.append((description, "#" + link))

    return toc_items


def create_toc(input_file_name, output_file_name, title=("##",)):
    """
    读取一个 md 文件并输出对应的目录
    :param input_file_name:
    :param output_file_name:
    :param title: 指定要创建目录的分级, 比如说 ("##", ) 就表示只为 ## 标题创建目录
    :return: None
    """
    with open(input_file_name, "r") as f:
        data = f.readlines()

    # 获取需要保存成 toc 的项
    title_list = get_title(data, title)

    # 获取 toc 需要的素材
    toc_items_list = get_toc_items(title_list)

    # 输出结果到文件
    with open(output_file_name, "w") as f:
        for each in toc_items_list:
            description, link = 0, 1  # 提高可读性的一行
            f.write("- [{}]({})\n".format(each[description], each[link]))


if __name__ == "__main__":
    test_file = "test_readme.md"
    test_out = "aaa.txt"
    create_toc(test_file, test_out)
