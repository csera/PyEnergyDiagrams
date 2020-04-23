import os
from setuptools import setup

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fh:
            return fh.read()
    except IOError:
        return ''

requirements = read('requirements.txt').splitlines()

setup(name='PyEnergyDiagrams',
      version='1.1.0',
      description='Script to construct energy level diagrams',
      url='https://github.com/tyiannak/pyAudioAnalysis',
      author='csera',
      author_email='',
      license='MIT License, 2017',
      packages=['PyEnergyDiagrams'],
      package_data={
        
      },
      zip_safe=False,
      install_requires=requirements,
      )