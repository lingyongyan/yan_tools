# coding=utf-8
"""
Program: data loader module
Description:
Author: Lingyong Yan
Date: 2018-12-27 20:12:28
Last modified: 2019-06-24 23:12:42
Python release: 3.6
Notes:
"""
import codecs
import os


def reader(file_path, encoding='utf-8'):
    ''' generator for read a file
    '''
    with codecs.open(file_path, 'r', encoding=encoding) as _file:
        for line in _file:
            yield line.strip()


def writer(file_path, datas, encoding='utf-8'):
    '''write datas to file_path.
    '''
    with codecs.open(file_path, 'w', encoding=encoding) as _file:
        for data in datas:
            _file.write(str(data) + '\n')


def load_data(file_path, dealer=lambda x: x):
    '''load data from file with dealer for every line.
    '''
    datas = []
    if os.path.exists(file_path):
        for line in reader(file_path):
            data = dealer(line)
            if data is not None:
                datas.append(data)
    else:
        print('%s not exists' % file_path)
    return datas


def parallel_load_data(file_paths, dealer=lambda x: x):
    '''load data from multi files with dealer for every line.
    '''
    datas = []
    for lines in zip(*map(reader, file_paths)):
        data = list(map(dealer, lines))
        if data is not None:
            datas.append(data)
    return datas


def sequential_load_data(file_paths, dealer=lambda x: x):
    '''load data from multi files with dealer for every line.
    '''
    datas = []
    for file_path in file_paths:
        print('load data from %s' % file_path)
        datas.extend(load_data(file_path, dealer=dealer))
    return datas


def save_data(file_path, datas, dealer=None):
    '''write data to file with dealer for every line.
    '''
    if dealer:
        datas = [dealer(data) for data in datas]
    writer(file_path, datas)


class DataDealer(object):
    def __init__(self):
        pass

    def pre_process(self, *arrays, **kwarrays):
        pass

    def post_process(self, *arrays, **kwarrays):
        pass

    def process(self, *array, **kwarrays):
        raise NotImplementedError

    def __call__(self, *array, **kwarrays):
        results = self.pre_process(*array, **kwarrays)
        results = self.process(results)
        results = self.post_process(results)
        return results
