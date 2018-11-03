from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
#         user = 'disco'
        user = request.form['nm'] 
        return redirect(url_for('success',name = user))
       
    else:
        user = request.form.get('nm', '')
        return redirect(url_for('success',name = user))

        
    
if __name__ == '__main__':
    app.run(debug = True)
