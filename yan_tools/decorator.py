# coding=utf-8
"""
Program:
Description:
Author: Lingyong Yan
Date: 2019-01-13 15:26:45
Last modified: 2019-01-13 15:31:44
Python release: 3.6
Notes:
"""
import warnings
from functools import wraps


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used."""
    @wraps(func)
    def wrapped(*args, **kwargs):
        """warpped doc"""
        warnings.simplefilter('always', DeprecationWarning)  # turn off filter
        warnings.warn("Call to deprecated function {}.".format(func.__name__),
                      category=DeprecationWarning,
                      stacklevel=2)
        warnings.simplefilter('default', DeprecationWarning)  # reset filter
        return func(*args, **kwargs)
    return wrapped
