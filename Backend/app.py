import flask
# Flask utils
from flask import Flask, redirect, url_for, request, render_template
import openai

#inserting the API key
openai.api_key = "{insert your key here}"
# from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer


import sqlite3
import requests
from flask_cors import CORS

conn = sqlite3.connect('res.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
print("Opened database successfully");
# Create table - CLIENTS
# c.execute('''CREATE TABLE RESPONSES
#              ([generated_id] INTEGER PRIMARY KEY, [Entry] text, [Response] text) ''')

conn.close()   
import random
from flask import jsonify
from flask_restful import reqparse

app = flask.Flask(__name__)
CORS(app)
app.debug = True

# @app.route("/", methods=['GET', 'POST'])
# def home():
#     # ins = request.form["insertion"]
#     return render_template("index.html")


#method called when the text is subkitted
@app.route('/get-text', methods=['GET', 'POST'])
def get_text():
    parser = reqparse.RequestParser()  # initialize


    parser.add_argument('ins', required=True)  # add arguments
    args = parser.parse_args() 
    print(args)

    # return args["ins"]
    ins = args["ins"]
    print(ins)

    # if request.method == "POST":
        #  temp = "Hello";
    # ins = request.form['insertion']
    response = "text received"      #only for debugging

    #davinci is the most expensive engine
    response = openai.Completion.create(
        engine="davinci",
        prompt=ins,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
        )
    print('Response received')
    response = response.choices[0].text
    print(response)
    conn = sqlite3.connect('res.db')  # You can create a new database by changing the name within the quotes
    c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
    response = response.replace("'", "")

    # "'" breaks the query
    ins = ins.replace("'", "")
    conn.execute(f"INSERT INTO RESPONSES (GENERATED_ID,ENTRY,RESPONSE) VALUES ({random.randint(1,10000000)}, '{ins}', '{response}' )");
    # print()
    conn.commit()
    conn.close()    
    # return render_template("index.html", res=response)

    # because in our frontend, we are using JavaScript and that uses the
    # async fetch, we return is JSON format as fetch receives the data in JSON
    return(jsonify({"text": response}))

app.run("0.0.0.0")