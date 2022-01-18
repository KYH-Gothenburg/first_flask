from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# We will use a factory function to avoid cyclic imports
def create_app():
    app = Flask(__name__)
    # Many parts of flask will require use to use a secret key so we create one
    app.config['SECRET_KEY'] = '123secret'
    # Will configure SQLAlchemy to use SQLite and the file db.sqlite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    # Init the SQLAlchemy object with our app object
    db.init_app(app)

    from blueprints.open import bp_open
    app.register_blueprint(bp_open)


    @app.get('/user')
    def user_get():
        return render_template("user.html")

    @app.post('/user')
    def user_post():
        return redirect(url_for('user_get'))

    return app



