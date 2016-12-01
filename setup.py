from setuptools import setup

setup(name='watchman',
      version='0.0.7',
      packages=['watchman'],
      entry_points={
          'console_scripts': [
              'watchman = watchman.main:main'
          ]
      },
      install_requires=[
        'colorama==0.3.7',
        'sh==1.12.0'
      ]
      )