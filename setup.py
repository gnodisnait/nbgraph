from setuptools import setup, find_packages

setup(name='nball4tree',
      version='0.1',
      description='nball for DAG embedding',
      url='http://github.com/gnodisnait/nbgraph',
      author='tiansi dong',
      author_email='tian1shi2@gmail.com',
      license='MIT',
      packages= find_packages(),
      package_data = {'': ['*.pickle'],},
      zip_safe=False)