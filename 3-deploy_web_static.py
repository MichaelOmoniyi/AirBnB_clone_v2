#!/usr/bin/python3
"""
creates and distributes an archive to your web servers, using
the function deploy
"""
from datetime import datetime
from fabric.api import *
from fabric.api import env
from fabric.api import put
from fabric.api import run
import os.path

env.hosts = ["35.153.50.129", "34.204.81.146"]


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


def deploy():
    """
    creates and distributes an archive to your web servers
    """

    archivePath = do_pack()
    if archivePath is None:
        return False
    return do_deploy(archivePath)
