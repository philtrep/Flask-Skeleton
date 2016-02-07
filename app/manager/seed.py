from flask.ext.script import Command


class seed(Command):

    def run(self):
        from app.database.seed import roles
