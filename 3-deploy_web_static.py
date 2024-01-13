#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""

do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('2-do_deploy_web_static').do_pack
from fabric.api import env


env.hosts = ['54.236.231.98', '54.197.46.38']


def deploy():
    """Creates and distributes an archive to web servers"""
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

if __name__ == "__main__":
    deploy()
