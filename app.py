from flask import Flask, render_template, redirect, session
import pymongo
from functools import wraps
from user import face_verify 

app = Flask(__name__)
app.secret_key = b''


#database
mongoURI = "mongodb+srv://"  # mongodb uri
client = pymongo.MongoClient(mongoURI)
database = client.get_database('flask_user_data1')
db = database.flask_user_login_data

FRmodel = face_verify.load_model()
# Decoders


def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/user/login')

  return wrap



#Routes
from user import routes

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template("dashboard.html")

