#py-amber_alert

Web Amber Alert framework for use in countries lacking alert infrastructure written in Python3 using Flask, Flask-SQLAlchemy and associated abstraction layers.

Please feel free to fork and contribute to the project. Currently, the project is a web app POSTGRES wrapper and has CRUD(Create, Read, Update and Delete) features and a public database view. 

py-amber_alert was created with the intention of its usage by both the authoritative body incharge in a country without a formal amber alert system as well as any involved Non-Govermental Organizations (NGOs) to track and aid in search and rescue of missing persons. The Amber Alert system operates on the principle of widening the search net by involving and using the public to ensure a faster response. It was originally designed to be implemented in India, but can be easily extended to any relevant situation or place. 

It is my hope that what I've hacked together will help the rising and rampant rates of kidnapping and missing persons cases in the aforementioned places.

##Quickstart
To get started working on the project, you'll need to have a POSTGRES db setup; the details of which you add to config.py under `SQLALCHEMY_DATABASE_URI`. 
Setting up the db is relatively straightforward, refer to the following that do a much better job than I could.
- [Arch Wiki](https://wiki.archlinux.org/index.php/PostgreSQL)
- [Dave Clark's Blog](http://clarkdave.net/2012/08/postgres-quick-start-for-people-who-know-mysql/)
- [Official PostgreSQL Documentation](https://www.postgresql.org/docs/9.4/static/tutorial-start.html)

Install dependencies with `pip install -r requirements.txt` (it is also advisable to be in a virtualenv while running pip).
To setup the db, run `python3 run.py init_db`; which initializes the db and writes the necessary trigger functions to the db.

You can access the functions by heading over to `localhost:5000`. Set up an admin account through `localhost:5000/register`, after which you can access the CRUD features through `localhost:5000/admin`. Of course, you can always access the functions through the navbar. 

##Future modifications and implementations
- Geotracking
- Beautification (have to learn how to make it look decently pretty.)
- Notification system 

##Contributors
Niranjan Ravichandra, @nravic. Again, please feel free to fork it, pull it, push it and bop it and add to the project. 
If you have any questions, you can send over an email or track me down on IRC, where I go by @nravic and usually trawl around #archlinux, #python, #emacs or #anime on freenode.

##LICENSE
Protected under the MIT licence. In short, do what you will with my code; just don't be an ass about it.
