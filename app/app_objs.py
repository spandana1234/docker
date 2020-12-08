#!/usr/bin/env python3.6
import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.main import create_app, db
app = create_app(os.getenv('CRUD_ENV') or 'dev')

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
