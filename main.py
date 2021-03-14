#!/usr/bin/env python

import subprocess


def getpath():
    return subprocess.run('pwd', shell=True)


def getfolders():
    return subprocess.run('ls -la', shell=True)


getfolders()
getpath()
