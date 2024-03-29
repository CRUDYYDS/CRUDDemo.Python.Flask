import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# postgresql://username:password@host:port/databasename
SQLALCHEMY_DATABASE_URI = "postgresql://root:123456@localhost:5432/postgres"
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Enable debug mode.
DEBUG = True







