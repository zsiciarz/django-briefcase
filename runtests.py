# -*- coding: utf-8 -*-

import os

from django.conf import settings


def make_absolute_path(path):
    return os.path.join(os.path.realpath(os.path.dirname(__file__)), path)


if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        SITE_ID = 1,
        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django_nose',
            'briefcase',
        ),
        TEMPLATE_DIRS = (
            make_absolute_path('example_project/templates'),
        ),
        ROOT_URLCONF = 'example_project.urls',
        TEST_RUNNER = 'django_nose.NoseTestSuiteRunner',
        NOSE_ARGS = ['--stop'],
    )


from django.core.management import call_command

call_command('test', 'briefcase')
