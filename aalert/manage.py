from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from aalert import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def init_db():
    """ DROPS AND RECREATES SQL SCHEMA
    """
    db.drop_all()
    db.configure_mappers()
    db.Model.metadata.create_all(db.session.connection())
    db.create_all()
    db.session.commit()
    
