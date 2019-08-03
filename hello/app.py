from flask import Flask


hello = Flask(__name__)
@hello.route('/', defaults={'who': 'master'})
@hello.route('/<who>')
def index(who):
    return '<h1>{} Welcome to my flask demo<h1>'.format(who)
