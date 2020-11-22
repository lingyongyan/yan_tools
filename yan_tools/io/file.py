# coding=utf-8
"""
Program:
Description:
Author: Lingyong Yan
Date: 2019-01-10 16:56:48
Last modified: 2019-01-10 17:10:58
Python release: 3.6
Notes:
"""
import os


def path_end_with(*end_strings):
    ends = end_strings

    def run(s):
        f = map(s.endswith, ends)
        if True in f:
            return s
    return run


def list_file_in_path(root_path, end_strings=[]):
    list_file = os.listdir(root_path)
    if end_strings:
        fil = path_end_with(*end_strings)
    else:
        def fil(x): return True
    f_file = filter(fil, list_file)
    f_file = map(lambda x: os.path.join(root_path, x), f_file)
    return list(f_file)
