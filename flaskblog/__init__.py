from flask import Flask
from email_validator import validate_email, EmailNotValidError
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = '4a95a87d5b0f3af5855f9cc161de54f2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)    # creating a database instance

from flaskblog import routes  
'''even though we fixed the problem with the messy imports by creating a package, we still have to watch for circular 
imports. Since our apps are importing this app variable above, we can't import the routes at the top of the file,
or else we will run into one of those circular imports again.
So we import after we have made the application initialization 
'''
