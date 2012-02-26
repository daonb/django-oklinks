django-oklinks
==============

This repository contains a Django pluggable app that save links for all the models. Ofri started this simple app when he found the existing apps too complex for Open-Knesset.

Installation
------------

::

  $ git clone https://daonb@github.com/daonb/django-oklinks.git
  $ cd django-oklinks
  $ python setup.py install

Testing
-------

::

  $ cd sample_project
  $ python manage.py test

Usage
-----

Checkout the doctest in oklinks.models.


Sample
------

This repository includes a simple Django project to demonstrate the use of oklinks to create a personal library of links for users. To run the project just::
  
  $ cd sample_project
  $ python manage.py runserver

And point your browser at http://127.0.0.1:8000/admin

