#!/usr/bin/python3
"""
This fabric script generates a .tgz archive from the
contents of the web_static folder of the AirBnB Clone repo

"""
from os import makedirs
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Generates the archive """
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    fp = "versions/web_static_{}.tgz".format(time_stamp)

    try:
        makedirs("./versions", exist_ok=True)
        local('tar -cvzf {} web_static'.format(fp))
        return fp

    except:
        return None
