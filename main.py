from flask import Flask, render_template, flash, request, redirect, url_for, session
from functions import *
from email_functions import *
app = Flask(__name__)
@app.route('/' , methods = ['GET' , 'POST'])
def index():
    sender_name = ""
    recipient_email_address = ""
    if (request.method == 'POST'):
        sender_name = request.form['sender']
        recipient_email_address = request.form['recipient']
        image_url = getDogPhoto()
        sendMail(sender_name, recipient_email_address, image_url)
    return render_template('landing_page.html')

if __name__ == "__main__":
    app.run(debug=True)
