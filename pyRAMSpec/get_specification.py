#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This is the main interface for get ram specification
"""

import os
import re
import json
import urllib

from dmidecode_output_parser import get_sys_info as get_linux_win_sys_info
from mac import get_sys_info as get_mac_sys_info

def get_ram_info():
    """TODO, split this function into multiple sub functions
    
    for windows and linux, use dmidecode
    and for mac, use the system_profiler
    
    http://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python
    """
    from sys import platform as _platform
    if _platform == "linux" or _platform == "linux2" or _platform == "win32":
        # linux or windows
        get_linux_win_sys_info() 
    elif _platform == "darwin":
        # OS X
        get_mac_sys_info()
    else:
        print "operating system that is not supported", _platform
