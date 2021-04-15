#!/usr/bin/python3
"""Module to deploy code to servers"""
import os
from fabric.api import local, put, run, env
from datetime import datetime


env.hosts = ['34.73.74.83', '35.196.176.70']
env.key_filename = 'private_key'


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


def do_deploy(archive_path):
    '''Function that distributes an archive to your web servers'''
    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path.split('/')[1]
        no_ext = archive.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive, path, no_ext))
        run('rm /tmp/{}'.format(archive))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False

def deploy():
    '''creates and distributes an archive to your web servers'''
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
