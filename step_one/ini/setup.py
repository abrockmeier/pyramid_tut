#!/usr/bin/env python3

from setuptools import setup

requires = [
    'pyramid',
]

setup(name='intro',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = intro:main
      """,
)
