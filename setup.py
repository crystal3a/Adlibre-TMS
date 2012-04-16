#!/usr/bin/env python

import os
import fnmatch

from setuptools import setup


def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
        )

def find_packages(path, base="" ):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package( dir ):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for base_name in files:
            if fnmatch.fnmatch(base_name, pattern):
                filename = os.path.join(root, base_name)
                if os.path.isfile(filename):
                    yield filename


setup(name='adlibre_tms',
    version='0.1.0',
    long_description=open('README.md').read(),
    url='https://github.com/macropin/Adlibre-TMS',
    packages=find_packages('.'),
    scripts=[],
    package_data={
            'adlibre_tms': ['LICENSE', 'adlibre_tms/templates/*.html',],
        },
    include_package_data=True,
    data_files = [
            ('adlibre_tms', ['local_settings.py', 'adlibre_tms/manage.py']),
            ('db', ['db/.gitignore']),
            ('deployment', find_files('deployment', '*')),
            ('docs', find_files('docs', '*')),
            ('www', find_files('www', '*')),
        ],
    install_requires=[
            'BeautifulSoup==3.2.0',
            'Django==1.3.1',
            'django-any==0.2.0',
            'django-compressor==1.1.1',
            'django-pagination==1.0.7',
            'django-uni-form==0.7.0',
            'flup==1.0.3.dev-20110405',
            'python-dateutil==2.0',
            'template-utils==0.4p2',
            'xml-models==0.5.1'
        ],
    dependency_links = [
        ],
)

print '****************************************************'
print find_files('adlibre_tms/templates', '*')