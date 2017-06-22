#!/usr/bin/env python
#-*- coding:utf-8 -*-

from setuptools import setup
import ccp

setup(name=ccp.__name__,
      version=ccp.__version__,
      author='Pongsakorn Sommalai',
      author_email='bongtrop@gmail.com',
      license='MIT',

      url='https://github.com/bongtrop/ccp',
      description='copy paste program with clip-server use stdin and stdout',
      long_description=ccp.__doc__,
      scripts=['ccp.py'],
      install_requires=[
       'requests',
       'docopt_dispatch',
       'pycrypto'
      ],
      entry_points="""
        [console_scripts]
        ccp=ccp:main
      """,
      keywords='copy paste tool'
     )
