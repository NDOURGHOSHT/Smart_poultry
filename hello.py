from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "le mot de passe que personne ne doit savoir "

#Creation de forme

class NamerForm(FlaskForm):
    name = StringField("Quel est ton nom :", validators=[DataRequired()])
    submit = SubmitField("submit")
 
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

    return render_template("name.html",
                           name = name,
                           form = form)

if __name__ == "__main__":
    app.run(debug=True) 





