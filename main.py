# importing flask modules
from flask import Flask , request , render_template , jsonify

# importing firebase_admin module
import firebase_admin

# importing firestore.py module to create firestore client
from firebase_admin import firestore

# importing credentials.py module from firebase_admin folder
from firebase_admin import credentials

# creating authentication file
cred = credentials.Certificate("write the path for your key")

# connect this python script/app with firebase using the authentication credentials
firebase_admin.initialize_app(cred)

# creating firestore client


# creating flask object
app = Flask(__name__)

# first api : index page, only GET requests allowed at this API 

        # getting values from firebase document

        # convert it to python dictionary format

        # extracting value from dictionary

        # rendering index.html template and pass the extracted value





# second api : adding data , only POST request allowed at this API

        # getting potentiometer value from esp32

        # sending potentiometer value on firebase

        # return status is json format




# start the server
if __name__  ==  "__main__":
    app.run(host = '0.0.0.0' , debug = True)

