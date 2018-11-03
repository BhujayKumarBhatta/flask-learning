from flask import Flask, request, session, redirect, url_for, escape

app = Flask(__name__)
app.secret_key = 'any secret key'

@app.route('/', methods = ['POST', 'GET'])
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
            "<b> <a href = '/logout'> clicl here to log out </a></b>"
    else:
        return "you are not logged in <b><a href = '/login'>click here to login</a></b>"          
             
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))  
    else:
        return '''
        <form action = " " method ="post">
          <p><input type = text name = username />
          <p><input type = submit value = login />
        </form>
        '''
@app.route('/logout', methods = ['POST', 'GET'])
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug = True)
    
    