DjanYolo
======

.. image:: https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FRoboMx%2Fdjanyolo&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false

Manage yolo images efficiently. A django app template that can be loaded to any existing app.

Features
-----
* Supports Django models
* Admin panel
* Image annotation
* Image cropping


Note
-----
This pypi is a part of #100DaysOfCode challenge. I needed to learn how packing are pushed and managed on pypi. So came up with simple module that was already cooked up. Check `original repo <https://github.com/MexsonFernandes/DjanYolo/>`__.

How to install?
-----


.. code:: python

    INSTALLED_APPS = (
        # ...
        'djanyolo',
    )
    
Register route
-----

.. code:: python
  from django.urls import include
  
  urlpatterns = [
        # ...
        url(r'^djanyolo$', include('djanyolo.urls')),
  ]
  
Have fun!
