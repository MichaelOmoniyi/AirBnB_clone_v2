#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the
function do_deploy
"""

from fabric.api import env
from fabric.api import put
from fabric.api import run
import os.path

env.hosts = [""35.153.50.129", "34.204.81.146"]


def do_deploy(archive_path):
    """ Distributes and archive to a web server

    Args:
        archive_path (str): The path of the archive file
    Returns:True if all operations have been done correctly,
    otherwise returns False
    """

    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    fileName = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(fileName)).failed is True:
        return False
    if run("tar -xzf /tmp{} -C /data/web_static/releases/{}/".
            format(file, fileName)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".
            format(fileName, fileName)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(FileName)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(FileName)).failed is True:
        return False
    return True
