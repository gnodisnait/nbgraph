from setuptools import setup, find_packages

setup(name='nbgraph',
      version='0.1',
      description='nball for DAG embedding',
      url='http://github.com/gnodisnait/nbgraph',
      author='gnod isnait',
      author_email='gnodisnait@gmail.com',
      license='MIT',
      packages= find_packages(),
      package_data = {'': ['*.pickle'],},
      zip_safe=False)