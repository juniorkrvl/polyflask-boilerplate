#!/usr/bin/env python
import os
from app import create_app #, db
from flask_script import Manager, Shell
# from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
# migrate = Migrate(app, db) We don't have database yet


def make_shell_context():
    return dict(app=app) # return dict(app=app, db=db, User=User, Role=Role) //We don't have models yet

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

manager.add_command("shell", Shell(make_context=make_shell_context))
#manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()