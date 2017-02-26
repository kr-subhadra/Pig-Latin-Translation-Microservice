import sys  #sys is imported in order to read the command line arguments
from flask import Flask, request
from flask import make_response
app = Flask(__name__)
length = len(sys.argv)
arguments = ""
if length == 1:
    arguments = ""
else:
    arguments = ' '.join(sys.argv[1:])   #Fetching the paragraph from the command line arguments

from FindPigLatin import *  #Importing the contents in FindPigLatin.py file

@app.route("/",methods=['GET'])     #Routing
def submit():
    if request.method == 'GET':
        text = arguments
        returned_sentence = convert_sentence(text)  #Calling the convert_sentence funtion in FindPigLatin.py file
        #Returning the Response, Status 200 indicates OK
        return make_response('''<html>
            <head>
            <body>''' + returned_sentence + '''</body>
                </head>
                </html>
                ''', 200)

if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)  #Running the app in Port 80
