# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request
#import png
import socket
import pyqrcode

#from pyqrcode import QRCode

# create the application object
app = Flask(__name__)

@app.route('/download', methods=['GET', 'POST'])
def download():
    return render_template('download.html')

@app.route('/')
def welcome():
    return render_template('welcome.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('download'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    IPAddr = "http://" + socket.gethostbyname(socket.gethostname()) + ":5000/login"
    url = pyqrcode.create(IPAddr)
    print(IPAddr)
    # Create and save the svg file naming "myqr.svg"
    url.svg("static/myqr.svg", scale=8)

    # Create and save the png file naming "myqr.png"
    url.png('static/myqr.png', scale=6)
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)
    #make a qr code the landing page of the desktop client, have it link to the welcome page. Then look through the file system and give a download button the thing to download the first file in there
