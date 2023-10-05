#!/usr/bin/python3
"""
This fabric script creates and distributes an archive to the web servers

"""
from os import makedirs, path
from datetime import datetime
from fabric.api import env, run, local, put

env.hosts = ['107.23.94.198', '35.175.64.25']


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

def do_deploy(archive_path):
    """ Distributes the archive

    Args:
        archive_path (str): path of the archive to be deploy on the servers
    """

    try:
        if not path.exists(archive_path):
            raise FileNotFoundError                                                     
        name = archive_path.split("/")[-1]
        name_no_ext = name.split(".")[0]

        remote = "/data/web_static/releases"
        dest = "{}/{}".format(remote, name_no_ext)

        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(dest))
        run('tar -xzf /tmp/{} -C {}'.format(name, dest))
        run('rm /tmp/{}'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(dest))

    except:
        print("Error. Version deploy aborted")
        return False

    print("New version deployed!")
    return True

def deploy():
    """ Generates and distributes the archive """
    if archive_to_deploy:
        return do_deploy(archive_to_deploy)
    else:
        return False

archive_to_deploy = do_pack()
