from flask_migrate import MigrateCommand
from flask_script import Manager, Server
from apps import create_app

app = create_app()

manager = Manager(app)

manager.add_command('run', Server())

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
