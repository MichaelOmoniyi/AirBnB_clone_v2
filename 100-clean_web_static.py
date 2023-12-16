#!/usr/bin/python3
# Delete out-of date archives
import os
from fabric.api import *

env.hosts = ["35.153.50.129", "34.204.81.146"]


def do_clean(number=0):
    """deletes out-of-date archives

    Args:
        number (int): number of the archives, including the most recent, to keep

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """

    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
    
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
