#!/usr/bin/python3
'''
    This sis a locked class
'''

class LockedClass:
    '''
       can only have one attribute first_name.
        Attribute: first_name (str): name
    '''
    __slots__ = ['first_name']
