from flask import Blueprint, render_template, redirect, url_for

# Create a blueprint object that can be used as an app object for this blueprint
bp_open = Blueprint('bp_open', __name__)


@bp_open.get('/')
def index():
    return render_template("index.html")


@bp_open.get('/login')
def login_get():
    return render_template('login.html')


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():

    return redirect(url_for('bp_open.login_get'))
