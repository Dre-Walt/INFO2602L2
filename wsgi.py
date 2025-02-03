import sys, click
from models import db, User
from app import app
from sqlalchemy.exc import IntegrityError


@app.cli.command("init", help="Creates and initializes the database")
def initialize():
  db.drop_all()
  db.create_all()
  bob = User('bob', 'bob@mail.com', 'bobpass')
  db.session.add(bob)
  db.session.commit()
  print(bob)
  print('database intialized')