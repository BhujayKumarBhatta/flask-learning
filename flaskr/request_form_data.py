# The data from a client’s web page is sent to the server as a global request object. 
#In order to process the request data, it should be imported from the Flask module.
# Important attributes of request object are listed below −
# Form − It is a dictionary object containing key and value pairs of form parameters and their values.
# args − parsed contents of query string which is part of URL after question mark (?).
# Cookies − dictionary object holding Cookie names and values.
# files − data pertaining to uploaded file.
# method − current request method.

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('request_form_data.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("request_form_data.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
   
   