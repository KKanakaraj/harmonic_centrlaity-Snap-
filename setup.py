#!/usr/bin/env python

from setuptools import setup

setup(name='harmonic_centrality_snap',
      version='0.2',
       description='Harmonic Centrality metric realization for snap',
       author='Kamalesh Kumar',
      url='https://github.com/asash/harmonic_centrality',
       packages=['harmonic_centrality_snap'],
       install_requires = [
              'Snap',
              'HLL'],
      )
