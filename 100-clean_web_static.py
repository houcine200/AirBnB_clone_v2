#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives using the function do_clean.
"""

from fabric.api import local, run, env, cd
import os

env.hosts = ['54.236.231.98', '54.197.46.38']


def do_clean(number=0):
    """
    Deletes all unnecessary archives in the versions folder and
    /data/web_static/releases folder of both web servers.
    """
    number = int(number)
    if number < 1:
        number = 1

    """"Delete local archives."""
    with cd("versions"):
        local_archives = local("ls -1").split("\n")
        local_archives_to_keep = local_archives[-number:]
        for archive in local_archives:
            if archive not in local_archives_to_keep:
                local("rm -f versions/{}".format(archive))

    """"Delete remote(server) archives."""
    with cd("/data/web_static/releases"):
        remote_archives = run("ls -1").split("\n")
        remote_archives_to_keep = remote_archives[-number:]
        for archive in remote_archives:
            if archive not in remote_archives_to_keep:
                run("rm -f /data/web_static/releases/{}".format(archive))
