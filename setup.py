#!/usr/bin/env python
# -*- coding: utf-8 -*-

import atexit
from subprocess import check_call

from setuptools import find_packages, setup
from setuptools.command.develop import develop
from setuptools.command.install import install


def _execute():
    check_call('pip install azure-cli --no-deps'.split())


class PostInstall(install):
    def run(self):
        atexit.register(_execute)
        install.run(self)


class PostDevelop(develop):
    def run(self):
        atexit.register(_execute)
        develop.run(self)

with open('CHANGELOG.md') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.readlines()

setup_requirements = [
]

test_requirements = [
]


setup(
    name='iotedgedev',
    version='1.1.0',
    description='The Azure IoT Edge Dev Tool greatly simplifies the IoT Edge development process by automating many routine manual tasks, such as building, deploying, pushing modules and configuring the IoT Edge Runtime.',
    long_description='See https://github.com/azure/iotedgedev for usage instructions.',
    author='Microsoft Corporation',
    author_email='vsciet@microsoft.com',
    url='https://github.com/azure/iotedgedev',
    packages=find_packages(include=['iotedgedev']),
    entry_points={
        'console_scripts': [
            'iotedgedev=iotedgedev.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license='MIT license',
    zip_safe=False,
    keywords='azure iot edge dev tool',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    cmdclass={'install': PostInstall, 'develop': PostDevelop}
)
