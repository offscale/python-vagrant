from ast import parse
from itertools import ifilter, imap
from os import path
from setuptools import setup

if __name__ == '__main__':
    package_name = 'python-vagrant'
    # parse version from package/module without importing or evaluating the code
    with open(path.join(package_name, '__init__.py')) as f:
        __author__, __author_email__, __version__ = imap(
            lambda buf: next(imap(lambda e: e.value.s, parse(buf).body)),
            ifilter(lambda line: (line.startswith('__version__') or
                                  line.startswith('__author__') or
                                  line.startswith('__author_email__')), f)
        )

    with open('README.md') as f:
        long_desc = f.read()

    setup(
        name=package_name,
        version=__version__,
        license='MIT',
        description='Python bindings for interacting with Vagrant virtual machines.',
        long_description=long_desc,
        keywords='python virtual machine box vagrant virtualbox vbox docker vmware vagrantfile',
        url='https://github.com/todddeluca/python-vagrant',
        author=__author__,
        author_email=__author_email__,
        classifiers=['License :: OSI Approved :: MIT License',
                     'Development Status :: 4 - Beta',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     ],
        packages=['vagrant'],
    )
