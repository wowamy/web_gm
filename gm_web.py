#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import cherrypy,os,time
import subprocess,signal
import threading

cwd = os.getcwd()

config = {
    'global' : {
        'server.socket_host' : '0.0.0.0',
        'server.socket_port' : 8080
    },
    '/': {
        'tools.sessions.on': True,
        'tools.staticdir.root': '%s' %cwd,
    },
    '/web/css': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': 'web/css',
    }
}

class RobotWeb(object):

    def __init__(self):
        self.ros_master = 'localhost'
        return

    @cherrypy.expose
    def index(self):
        return open('./web/home.html')
    
    @cherrypy.expose
    def start(self):
        subprocess.Popen(['bash ./bash_script/gm.bash '+self.ros_master], shell=True)
        return open('./web/stop.html')

    @cherrypy.expose
    def stop(self):
        os.system("ps aux | grep pub | awk '{print $2}' | xargs kill -9")
        return 'stop Gmapping'

if __name__ == "__main__":
    cherrypy.quickstart(RobotWeb(), '/',config)