Social Help API
=================
Developer : Khairi Brahmi
***
Phone : +21622449506
==========


Getting Up and Running Locally With Docker
==========================================
 
The steps below will get you up and running with a local development environment.
All of these commands assume you are in the root of your project.


Prerequisites
-------------

* Docker 
* Docker Compose 
 
 
Build the Stack
---------------

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f local.yml build 
    
    
Reset and load data to the database
---------------------------
 
    $ docker system prune --volumes
    $ docker-compose -f local.yml up
    $ docker-compose -f local.yml run --rm django python manage.py load_data
    $ now you have an admin user :  email=admin@admin.com , password=password
    http://127.0.0.1:8001/
 
Run the Stack
-------------

This brings up both Django and PostgreSQL. The first time it is run it might take a while to get started, but subsequent runs will occur quickly.

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f local.yml up
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py test 
    $ docker-compose -f local.yml run --rm django pytest
    $ docker-compose -f local.yml run --rm django python manage.py shell_plus --notebook
    $ Go to localhost:8001
    $ docker-compose -f local.yml run --rm django coverage run -m pytest
    $ docker-compose -f local.yml run --rm django coverage report
    
    Account.objects.filter(lft=F('rght')-1)
Execute Management Commands
---------------------------

As with any shell command that we wish to run in our container, this is done using the ``docker-compose -f local.yml run --rm`` command: ::

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    $ docker-compose -f local.yml run --rm django python manage.py makemigrations
    $ docker-compose -f local.yml run --rm django python manage.py shell_plus
Here, ``django`` is the target service we are executing the commands against.

 

Backups
-------------
    $ docker-compose -f local.yml exec postgres backup
    $ docker cp 50b27d25021e:/db.json ./app/db.json
    $ docker- ps
    $ docker cp 5e9b64676deb:/backups ./backups
    $ docker-compose -f local.yml exec postgres restore backup_2020_06_02T08_18_57.sql.gz

Removing All Unused Objects
-------------
    $ docker stop $(docker ps -a -q)
    $ docker rm $(docker ps -a -q)
    $ docker system prune
    $ docker system prune --volumes
    

