# -*- coding: utf-8 -*-
"""
    Flask-WebSocket
    ~~~~~~~~~~~~~~~~~~~~

    copyright: (c) 2017 by Damon Chen.
    license: BSD, see LICENSE for more details.

    simple websocket for Flask
"""


from setuptools import setup
description = open('README').read()

setup(
    name='Flask-WebSocket',
    version='0.1',
    url='http://github.com/damonchen/flask-websocket/',
    license='BSD',
    author='Damon Chen',
    author_email='netubu@gmail.com',
    description='simple websocket for Flask',
    long_description=description,
    py_modules=['flask_websocket'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)