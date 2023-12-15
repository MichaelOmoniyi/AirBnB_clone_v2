#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack
"""
from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Generates the .tgz archive
    """
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")

        archive = ("web_static_{}".format(timestamp))

        local("tar -czvf versions/{}.tgz web_static".format(archive))

        return "versions/{}.tgz".format(archive)
    except Exception as e:
        return None
