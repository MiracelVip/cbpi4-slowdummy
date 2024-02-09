from setuptools import setup

setup(name='cbpi4-slowdummy',
      version='0.0.2',
      description='Sensor with slow increasing value',
      author='MiracelVip',
      author_email='',
      url='https://github.com/MiracelVip/cbpi4-slowdummy',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-slowdummy': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-slowdummy'],
     )