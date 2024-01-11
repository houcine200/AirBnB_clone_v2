#!/usr/bin/python3
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a .tgz archive from the contents of web_static folder."""
    file_name = f"web_static_{datetime.now():%Y%m%d%H%M%S}.tgz"

    local("mkdir -p versions")
    """tar -czvf archive_name.tgz web_static"""
    local(f"tar -cvzf versions/{file_name} {'web_static'}")
    return f"versions/{file_name} {'web_static'}"
