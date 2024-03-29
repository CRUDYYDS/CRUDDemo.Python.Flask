# Description
This is a sample project for flask crud api. You can to start your porject by reference this project. Is a good start for new user of flask.

# Install packages
pip install -r requirements.txt

# Database config
edit config.py to config database

## Initial database
flask db init

flask db migrate

flask db upgrade

Undo upgrade by:

flask db downgrade

# Launch 
flask run

# Call api
use postman or any httpclient to call url with http://127.0.0.1:5000/users/add  ..
