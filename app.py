from flask import Flask, render_template, redirect, session
import pymongo
from functools import wraps


app = Flask(__name__)
app.secret_key = b',\x96\xf4\xf1\x1fv\x19\xb0e\x9al\x8aUR\x14\x0c'


#database
mongoURI = "mongodb+srv://"  # mongodb uri
>>>>>>> Stashed changes
client = pymongo.MongoClient(mongoURI)
database = client.get_database('flask_user_data1')
db = database.flask_user_login_data

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

