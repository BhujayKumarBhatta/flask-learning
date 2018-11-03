from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', user = name)

@app.route('/dict2table')
def dict2table():
    dict = {'phy':50,'che':60,'maths':70}
    return render_template('dict2table.html', data = dict)


if __name__ == '__main__':
    app.run(debug = True)
    