#!/usr/bin/env python

from distutils.core import setup

setup(name='google-translate',
      version='0.01',
      description='Google Translate API reverse-engineered from chromium and google translate widget',
      author='Victor Gavro',
      author_email='vgavro@gmail.com',
      url='http://bitbucket.org/vgavro/google_translate',
      py_modules=['google_translate'],
      scripts=['google_translate.py'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='translate text google',
     )
