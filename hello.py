from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = "le mot de passe que personne ne doit savoir "
# ajout d'un database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
#Initialisation du database
db = SQLAlchemy(app)

#Creation de modele
class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.now)
    
    #Cree un String
    def __repr__(self):
        return '<name %r>' % self.name

#Creation de forme

class UserForm(FlaskForm):
    name = StringField("Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    submit = SubmitField("submit")

class NamerForm(FlaskForm):
    name = StringField("Quel est ton nom :", validators=[DataRequired()])
    submit = SubmitField("submit")
 


@app.route('/user/add', methods=['GET','POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
       user = Users.query.filter_by(email=form.email.data).first()
       if user is None:
        user = Users(name=form.name.data, email=form.email.data)
        db.session.add(user) 
        db.session.commit()
        name = form.name.data
        form.name.data= ''
        form.email.data= ''
        flash("Utilisateur ajouter avec succes!!!")
    our_users= Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form=form, name=name,
                           our_users=our_users )
@app.route('/')
def index():
    first_name = "ndour"
    stuff = " This is Bold text "
    favorite_pizza = ["mango","limon","khall",41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza = favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #validation de la forme
    if form.validate_on_submit():
        name= form.name.data
        form.name.data = ''
        flash("Bienvenue dans notre page web !!!")



    return render_template("name.html",
                           name = name,
                           form = form)

if __name__ == "__main__":
    app.run(debug=True) 





