from flask import Flask,redirect,url_for
# from werkzeug import 
# from flask.helpers import 

app  = Flask(__name__)


@app.route('/<name>')
def greetings(name):
    return 'greetings %s' % name

@app.route('/blog/<int:postID>')
def blog(postID):
    return 'this is blog number %d' % postID

@app.route('/owner')
def welcome():
    return 'welcome to your house '

@app.route('/guest/<guest>')
def hello(guest):
    return 'hello  %s, whom do you want to meet ?' % guest

@app.route('/entry/<person>')
def entry(person):
    if person == 'owner':
        return redirect(url_for('welcome'))
    else:
        return redirect(url_for('hello', guest = person))

if __name__ == '__main__':
    app.run(debug = True)