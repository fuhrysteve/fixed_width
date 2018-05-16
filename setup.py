try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='fixed_width',
    version='0.1.0',
    description='Parse fixed-width files in python',
    long_description=readme,
    author='Stephen J. Fuhry',
    author_email='fuhrysteve@gmail.com',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    url='https://github.com/fuhrysteve/fixed_width',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
