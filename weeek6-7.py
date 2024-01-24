from pymongo.mongo_client import MongoClient
from flask import request,Flask,jsonify

uri = "mongodb+srv://Pawarit:PS1234@cluster0.xox3wyk.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully ")
except Exception as e:
    print(e)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"


if __name__ == '__main__' :
    app.run(host = "0.0.0.0", port = 5000,debug = True )