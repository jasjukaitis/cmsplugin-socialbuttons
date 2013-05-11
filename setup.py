import os

from setuptools import setup, find_packages

setup(
    name='cmsplugin-socialbuttons',
    version='0.1.2',
    description='A simple plugin for adding social buttons.',
    long_description=open(os.path.join(os.path.dirname(__file__),
                                       'README.rst')).read(),
    author='Raphael Jasjukaitis',
    author_email='webmaster@raphaa.de',
    url='https://github.com/jurheinsieg/cmsplugin-socialbuttons',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    include_package_data=True
)
