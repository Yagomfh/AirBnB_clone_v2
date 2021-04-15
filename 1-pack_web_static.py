#!/usr/bin/python3
"""script that generates a .tgz archive"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    '''Function that generates tgz archive'''
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(date)
        local('tar -cvzf {} web_static'.format(archive_name))
        return archive_name
    except:
        return None
