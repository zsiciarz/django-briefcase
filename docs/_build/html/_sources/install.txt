============
Installation
============

Get the code
============

You can install the package from PyPI::

    pip install django-briefcase
    
or::

    easy_install django-briefcase

Any packages that ``django-briefcase`` depends on, will be automatically 
downloaded (currently this is Django and South).

Stable releases are located at PyPI. The development version can be installed 
from Github_::

    git clone git://github.com/zsiciarz/django-briefcase.git
    cd django-briefcase
    python setup.py install

or if you're using pip_::

    pip install -e git+git://github.com/zsiciarz/django-briefcase.git#egg=django-briefcase

.. _Github: http://github.com/zsiciarz/django-briefcase
.. _pip: http://pip.openplans.org/


Configure your project
======================

Add ``briefcase`` to your ``INSTALLED_APPS`` in ``settings.py``. Then, run
``python manage.py migrate briefcase`` to create document-related database 
tables.

.. note::
   If you don't use South, run ``python manage.py syncdb``, however
   using South to handle your database schema history is recommended.
