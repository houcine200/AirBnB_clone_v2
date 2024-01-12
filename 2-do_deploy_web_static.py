#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers"""

from datetime import datetime
from os import path
from fabric.api import local, put, run, env

env.hosts = ['54.236.231.98', '	54.197.46.38']


def do_pack():
    """Create a .tgz archive from the contents of web_static folder."""
    archive_filename = f"web_static_{datetime.now():%Y%m%d%H%M%S}.tgz"
    archive_path = f"versions/{archive_filename}"

    local("mkdir -p versions")
    local(f"tar -cvzf {archive_path} web_static")
    return archive_path


def do_deploy(archive_path):
    """Distribute an archive to web servers."""
    try:
        if not path.exists(archive_path):
            return False

        put(archive_path, "/tmp/")

        filename = archive_path.split("/")[-1]
        folder_name = f"/data/web_static/releases/{filename.split('.')[0]}"
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(filename, folder_name))

        run("rm /tmp/{}".format(filename))

        run("mv {}/web_static/* {}".format(folder_name, folder_name))

        run("rm -rf {}/web_static".format(folder_name))

        run("rm -rf /data/web_static/current")

        run("ln -s {} /data/web_static/current".format(folder_name))

        print("Deployment successful!")
        return True

    except Exception as err:
        print(err)
        return False
