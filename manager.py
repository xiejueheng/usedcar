#!/usr/bin/env python
# coding: utf-8

import os
from flask_script import Manager, Server
from usedcar.app import create_app

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


settings = os.path.abspath('./etc/settings.py')
if not os.path.exists(settings):
    settings = os.path.abspath('./etc/dev_config.py')

if 'JUNE_SETTINGS' not in os.environ and os.path.exists(settings):
    os.environ['JUNE_SETTINGS'] = settings

manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('runserver', Server(host='0.0.0.0'))


@manager.command
def createdb():
    """Create database for june."""
    from usedcar.models import db
    db.create_all()

'''
@manager.command
def live(port=5000):
    from livereload import Server
    server = Server(manager.create_app())
    server.watch('assets/*.js', 'make -C assets build')
    server.watch('assets/page/*.js', 'make -C assets build')
    server.watch('assets/stylus', 'make -C assets stylus')
    server.serve(port)
'''


if __name__ == '__main__':
    manager.run()
