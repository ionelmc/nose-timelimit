# -*- encoding: utf8 -*-
from setuptools import setup, find_packages

import os

setup(
    name = "nose-timelimit",
    version = "0.1.2",
    url = 'https://github.com/ionelmc/nose-timelimit',
    download_url = '',
    license = 'BSD',
    description = "Nose module that reorders tests so the quickest are run first.",
    long_description = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author = 'Ionel Cristian Mărieș',
    author_email = 'contact@ionelmc.ro',
    py_modules = ['nosetimelimit'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        "nose>=0.10",
    ],
    entry_points = {
        'nose.plugins.0.10': [
            'nosetimelimit=nosetimelimit:TimeLimitPlugin'
        ]
    },
)
