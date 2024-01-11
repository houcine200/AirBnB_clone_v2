#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a .tgz archive from the contents of web_static folder."""
    file_name = f"web_static_{datetime.now():%Y%m%d%H%M%S}.tgz"
    archive_path = f"versions/{file_name}"

    local("mkdir -p versions")
    local(f"tar -cvzf {archive_path} web_static")
    return archive_path
