from flask import Flask ,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:Srinadh@123@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://cwknipuhfdcjdm:e63da809b2e47c1e2eb7d497d7a2f383610af66877978659ebd61dbfe9518227@ec2-52-50-171-4.eu-west-1.compute.amazonaws.com:5432/d3vn9kmfojsrsk'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


db = SQLAlchemy(app)

class Favquotes(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	author = db.Column(db.String(30))
	quote = db.Column(db.String(2000))


@app.route('/')
def index():
	result = Favquotes.query.all()
	return render_template('index.html',result=result)


@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')

@app.route('/process', methods =['POST'])
def process():
	author = request.form['author']
	quote = request.form['quote']
	quotedata =Favquotes(author=author,quote=quote)
	db.session.add(quotedata)
	db.session.commit()

	return redirect(url_for('index'))




   	  #else:
		 #return render_template('quotes.html')
