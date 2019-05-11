from flask import *
from healthy import Myfood
from bson.objectid import ObjectId
app = Flask(__name__)


@app.route('/')
def index():
  foods = Myfood.find()
  return render_template('index.html',all_foods=foods)

@app.route('/homepage')
def home():
  foods = Myfood.find()
  return render_template('homepage.html',all_foods=foods)
@app.route('/detailfood/<id>')
def detail(id):
  detail_food = Myfood.find_one({'_id': ObjectId(id)})
  return render_template('detailfood.html',food=detail_food)
  
@app.route('/tinhcalo')
def tinhcalo():
  return render_template('cal_bmr.html')

if __name__ == '__main__':
  app.run(debug=True)
 