# Django-nonrel boilerplate application for the Google App Engine

Since you must include your dependencies in any GAE application, you can clone this repository to start your django-nonrel GAE application.

To get started:

`mkdir myproject
cd myproject
git clone git://github.com/colinsullivan/google-app-engine-django-nonrel-boilerplate.git
mv google-app-engine-django-nonrel-boilerplate/ myprojectapp
cd myprojectapp/
git submodule update --recursive
./manage.py runserver
`

I didn't write any of this code.  Information about included packages (in lib/ directory):

* [djangoappengine installation](http://www.allbuttonspressed.com/projects/djangoappengine#installation) on allbuttonspressed.com
    * django-nonrel: [https://github.com/adieu/django-nonrel](https://github.com/adieu/django-nonrel)
    * djangoappengine: [https://github.com/adieu/djangoappengine](https://github.com/adieu/djangoappengine)
    * djangotoolbox: [https://github.com/adieu/djangotoolbox](https://github.com/adieu/djangotoolbox)
    * django-dbindexer: [https://github.com/adieu/django-dbindexer](https://github.com/adieu/django-dbindexer)
    * django-testapp: [https://github.com/colinsullivan/django-testapp](https://github.com/colinsullivan/django-testapp)
        * (not in lib/ directory, just files in ./)
* gaeunit: [https://github.com/colinsullivan/gaeunit](https://github.com/colinsullivan/gaeunit)

Feedback is appreciated.