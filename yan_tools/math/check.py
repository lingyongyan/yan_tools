# coding=utf-8
"""
Program: data loader module
Description:
Author: Lingyong Yan
Date: 2019-06-02 20:12:28
Last modified: 2019-06-02 22:02:14
Python release: 3.6
Notes:
"""

def is_number(num):
    try:
        float(num)
        return True
    except:
        return False
