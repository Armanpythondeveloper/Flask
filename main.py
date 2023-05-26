from flask import Flask
from flask import render_template
from forms import RegistrationForm,LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '63b872336cf28fa9eb97489a972bcdae'
"""
shell-i mej
python
import secrets
secrets.token_hex(16)

"""

posts = [

    {
        'author':'Hovhannes Tumanyan',
        'title':'BLOG POST 1',
        'date':'april,21,2020',
        'content':'Fist blog '
    },
     {
        'author':'Avetiq Isahakyan',
        'title':'BLOG POST 2',
        'date':'april,21,2020',
        'content':'Second blog '

    }


]



@app.route('/')

def home():

    return render_template('main/home.html',posts=posts)

@app.route('/about')

def about():
    return render_template('main/about.html')


@app.route('/register',methods = ['GET','POST'])

def register():
    form = RegistrationForm()

    return render_template('main/register.html',form = form)


@app.route('/login')

def login():
    form = LoginForm()

    return render_template('main/login.html',form = form)


if __name__ == '__main__':

    app.run(debug=True)