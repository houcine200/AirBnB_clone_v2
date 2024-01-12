#!/usr/bin/python3
from datetime import datetime
from os import path
from fabric import local, put, run, env

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
        archive_filename = archive_path.split("/")[-1].split(".")[0]
        release_path = f"/data/web_static/releases/{archive_filename}"
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{archive_filename}.tgz -C {release_path}\
            --strip-components=1")

        run(f"rm /tmp/{archive_filename}.tgz")

        current_path = "/data/web_static/current"
        run(f"rm -f {current_path}")
        run(f"ln -s {release_path} {current_path}")

        print("Deployment successful!")
        return True

    except Exception as err:
        print(err)
        return False
