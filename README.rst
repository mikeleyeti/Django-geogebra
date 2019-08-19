=====
Geogebra
=====

Geogebra is a simple Django app to include Geogebra iframe in a Django site.


Quick start
-----------

1. Add "Geogebra" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'geogebra',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('geogebra/', include('geogebra.urls')),

3. Run `python manage.py migrate` to create the geogebras models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a geogebra (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/geogebra/ 
