from flask import Flask, render_template, request, redirect, url_for, abort
# Initialize the Flask application
app = Flask(__name__)
 
 
@app.route('/')
def index():
   return render_template('log_in.html')
    
@app.route('/login',methods = ['POST', 'GET']) 
def login(): 
   if request.method == 'POST' and request.form['txtemail'] == 'tutorial101@blogspot.com' and request.form['txtpass'] == 'ednalan' :
      return redirect(url_for('success'))
   else:
      abort(401)
 
@app.route('/success')
def success():
   return '<h1>logged in successfully</h1>'
  
   
if __name__ == '__main__':
   app.run(debug = True)
   