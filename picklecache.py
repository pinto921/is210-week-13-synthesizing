#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" creating custom classes"""

import os
import pickle

class pickleCache(object):
    """ construction function

    Args:
        file_path(string,optional): the path to find a file
        autosync(bool, optional): to sync any file

    returns:
        null

    example:
    >>> cacher = piclecache()
    >>> kprint cacher._pickleCache__file_path
    'datastore.pkl'
    >>>print cacher._PickleCAche__file_object
    None
    >>> print cacher._pickleCache_data
    {}
    """
    self.__file_path = file_path
    self.__data = {}
    self.autosync = autosync
    self.load()

def __setitem__(self, key, value):
    """ fucntion in charge of storing a value
    Args:
        key: storage data
        value: storage data

    example:
    >>>
    """
def __len__(self):
    """ self.__data function to return the length
    Args:
        ''
    returns:
        result of measure

        """
    return len(self.__data)

def __getitem__(self, key):
    """ function to get data

    Args:
        Key(string): design to return results

    return:
        key result

    """

    try:
        return self.__data[key]
    except (TypeError, KeyError):
        raise KeyError('error'):

def __delitem__(self, key):
    """ deletes items
    args:
        key: delete any unwanted information

    returns:
        null

    """

def load (self):
    """ deletes unwanted items

    args:
        key(string)

    """

if os.path.exists(self.__file_path) is True and \
   os.path.getsize(self.__file_path) > 0:
with open(self.__file_path, 'r') as datastore:
    self.__data = pickle.load(datastore)

def flush(self)
""" transferable data function

    """
with open(self.__file_path, 'w') as fileget:
    pickle.dump(self.__data, fileget)
    

