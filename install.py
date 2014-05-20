#!/usr/bin/env python

import subprocess


def main():
    # Install system dependencies
    subprocess.call(["apt-get", "update"])
    subprocess.call(["apt-get", "-y", "upgrade"])
    subprocess.call(["apt-get", "-y", "install", "upstart"])
    subprocess.call(["apt-get", "-y", "install", "python-dev"])
    subprocess.call(["apt-get", "-y", "install", "python-pip"])

    # Setup the virtualenv
    subprocess.call(["pip", "install", "virtualenv"])
    subprocess.call(["virtualenv", "env", "--no-site-packages"])

    # Make default images folder
    subprocess.call(["mkdir", "/home/pi/images"])

    # Copy Upstart scripts
    subprocess.call(["cp", "upstart/dropbox-worker.conf", "/etc/init"])
    subprocess.call(["cp", "upstart/time-lapse.conf", "/etc/init"])

    print("Installation of system dependencies is complete!")
    print("Next steps...")
    print("1.) activate the virtualenv: source ./env/bin/activate")
    print("2.) install requirements: pip install -r requirements.txt")
    print("3.) reboot your Pi: sudo reboot")


if __name__ == '__main__':
    main()