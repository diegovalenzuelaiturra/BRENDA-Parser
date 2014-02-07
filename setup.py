#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import absolute_import

import versioneer
from setuptools import setup


# All other arguments are defined in `setup.cfg`.
setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass()
)
