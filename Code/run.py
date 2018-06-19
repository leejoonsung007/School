import os
from flask_migrate import Migrate
from app import create_app
from app import db
from app.models.Roleomg import Role
from app.models.User import User
from app.models.School import School
from app.models.User_operation import Follow
from app.models.School_rank import Rank2017
from app.models.Pro2015 import Pro2015
from app.models.Pro2016 import Pro2016
from app.models.Pro2017 import Pro2017
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, School=School,
                Rank2017=Rank2017, Pro2017=Pro2017, Pro2016=Pro2016,
                Pro2015=Pro2015, Follow=Follow)


if __name__ == '__main__':
    app.run(debug=True)
