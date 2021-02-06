import flask
import pymongo
from flask import Flask, escape, request,jsonify
import requests
import json
import logging

app = Flask(__name__)

#connection to mongodb database,
client = pymongo.MongoClient("mongodb+srv://dbnumadic:Numadic@cluster0.qinim.mongodb.net/test?retryWrites=true&w=majority")

db = client.theguardian
collection = db.news


#running flask
@app.route('/', methods=['GET'])
def get():

    news = collection.find()
    response = []
    for new in news :
        new['_id'] = str(new['_id'])


        response.append(new)
    return flask.jsonify(response)



if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port = 8100)
    app.run(debug=True)