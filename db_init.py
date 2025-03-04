import dotenv
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

dotenv.load_dotenv()
db_pass = os.environ.get('DB')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://bee0263bfc535e:{db_pass}@us-cdbr-east-03.cleardb.com/heroku_c02aad4223f7e7a'
app.config['SQLALCHEMY_POOL_RECYCLE'] = 60
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'writeenkeykavishiandsushaan'
app.config['UPLOAD_FOLDER'] = 'static/'
db = SQLAlchemy(app)

class Users(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(30),  nullable = False)
  password = db.Column(db.String(300), nullable = False) 
  email = db.Column(db.String(50), nullable = False)

class Posts(db.Model):
  post_id = db.Column(db.Integer, primary_key = True)
  post_title = db.Column(db.String(500), nullable = False)
  post_genre = db.Column(db.String(30), nullable = False)
  post_content = db.Column(db.Text(60000), nullable = False)
  post_media = db.Column(db.String(1000), nullable = True)
  post_citation = db.Column(db.String(1000), nullable = True)
  post_anonymity = db.Column(db.String(5), nullable = False)
  post_creator = db.Column(db.String(30), nullable = False)
  post_publishtime = db.Column(db.String(50), nullable = False)
  post_liked_by = db.Column(db.String(60000), nullable = False) 
  post_netlikes = db.Column(db.Integer, nullable = False)
