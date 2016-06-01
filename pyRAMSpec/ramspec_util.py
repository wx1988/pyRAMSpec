#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
This file contain some common utility functions
"""

import subprocess
import webbrowser


def execute_cmd(cmd):
    """execute a command line command and get the output

    :return : Returns output strings
    """
    process = subprocess.Popen(cmd,\
        stdout=subprocess.PIPE,\
        stderr=subprocess.PIPE)
    out, _ = process.communicate()
    out = out.replace("\r\n", "\n")
    return out

def redirect_to_recommend():
    """Get the system information and redirect to recommendation website
    """
    from get_specification import get_ram_info
    sys_info =  get_ram_info()
    #print sys_info

    url_tpl = "http://rtds9.cse.tamu.edu:8080/suggest?sys_info=%s"
    #json_str = json.dumps(sys_info)

    the_url = url_tpl%(urllib.quote_plus(json.dumps(sys_info)))

    print the_url
    #the_url.replace("")
    #os.system("explorer %s"%(the_url))

    webbrowser.open(the_url)


