from setuptools import setup

setup(name='watchman',
      version='0.0.1',
      packages=['watchman'],
      entry_points={
          'console_scripts': [
              'watchman = watchman.main:main'
          ]
      },
      )