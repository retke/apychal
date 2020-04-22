from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.rst")) as f:
    long_description = f.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name = "apychal",
    description = "Aysync version of pychallonge",
    long_description = long_description,
    author = "Wonderfall",
    author_email = "wonderfall@protonmail.com",
    url = "https://github.com/Wonderfall/pychal",
    license = "Public Domain",
    version = "1.9.0",
    keywords = ['tournaments', 'challonge'],
    packages = find_packages(),
    platforms=['any'],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires = requirements
)
