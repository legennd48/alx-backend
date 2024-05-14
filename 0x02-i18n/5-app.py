#!/usr/bin/env python3
'''
Basic Babel setup
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config():
    '''
    babel app cnfiguration
    '''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    '''
    returns a user dictionaru or None if the ID cannot
    be found or if login_as is not passed
    '''
    login = request.args.get('login_as')
    if login:
        return users.get(int(login))
    return None


@app.before_request
def before_request() -> None:
    '''
    initialise user to Flask.g.user
    '''
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    '''
    uses request.accept_languages to determine
    the best match for supported languages
    '''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def basic() -> str:
    '''
    basic route
    '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
