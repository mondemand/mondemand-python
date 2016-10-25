#!/usr/bin/env python

"""
setup.py file for Mondemand binding
"""

from distutils import sysconfig
from distutils import log
from distutils.core import setup
from distutils.core import Command

import os
from subprocess import call, Popen, PIPE

BASEPATH = os.path.dirname(os.path.abspath(__file__))
USER_OPTIONS = [('bs', None, None)]

def runner(cmd, skip_errors=False):
    resp = Popen(cmd,
                 cwd=BASEPATH, stdout=PIPE, stderr=PIPE).communicate()
    log.info(resp[0])
    if resp[1] and not skip_errors:
        log.error(resp[1])

class MakeCommand(Command):
    user_options = USER_OPTIONS
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass

class MakeAll(MakeCommand):
    def run(self):
        runner(['make', 'all'])

class MakeBuild(MakeCommand):
    user_options = USER_OPTIONS
    def run(self):
        runner(['make', 'build'])

class MakeInstall(MakeCommand):
    user_options = USER_OPTIONS
    def run(self):
        runner(['make', 'install'])

class MakeClean(MakeCommand):
    user_options = USER_OPTIONS
    def run(self):
        runner(['make', 'clean'], skip_errors=True)

setup(
    name='mondemand',
    version='0.0.2',
    description='MonDemand python bindings',
    license='BSD',
    url='http://www.mondemand.org/',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],

    cmdclass={
        'all': MakeAll,
        'build': MakeBuild,
        'install': MakeInstall,
        'clean': MakeClean,
    }
)
