import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-briefcase',
    version=__import__('briefcase').__version__,
    description='Yet another document management app for Django.',
    long_description=read('README.rst'),
    author='Zbigniew Siciarz',
    author_email='antyqjon@gmail.com',
    url='http://github.com/zsiciarz/django-briefcase',
    license='MIT',
    install_requires=['Django', 'south'],
    packages=[
        'briefcase',
        'briefcase.migrations',
    ],
    package_data = {'': ['data/mime.types']},
    include_package_data=True,
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Utilities'],
)
