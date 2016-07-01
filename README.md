py-amber_alert
Web Amber Alert framework for use in countries lacking alert infrastructure written in Python using Flask, Flask-SQLAlchemy and associated abstraction layers.

Please feel free to fork and contribute to the project. Currently, the project is a web app POSTGRES wrapper and has CRUD(Create, Read, Update and Delete) features and a public database view. 

Quickstart
To get started working on the project, you'll need to have a POSTGRES db setup; the details of which you add to config.py under `SQLALCHEMY_DATABASE_URI`. 
Setting up the db is relatively straightforward, refer to the following that do a much better job than I could.
- [Arch Wiki](https://wiki.archlinux.org/index.php/PostgreSQL)
- [Dave Clark's Blog](http://clarkdave.net/2012/08/postgres-quick-start-for-people-who-know-mysql/)
- [Official PostgreSQL Documentation](https://www.postgresql.org/docs/9.4/static/tutorial-start.html)


Future modifications and implementations
- Geotracking
- Beautification (have to learn how to make it look decently pretty.)
- Notification system 
