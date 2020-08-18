from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import psycopg2

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_stuff'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbgqysgi:I1TguOyGq7W1hDPkPvy3fvTSKckO_566@ruby.db.elephantsql.com:5432/dbgqysgi'

db = SQLAlchemy(app)

from JobDoc import routes