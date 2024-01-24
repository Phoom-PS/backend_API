from pymongo.mongo_client import MongoClient
from flask import request,Flask,jsonify
from flask_basicauth import BasicAuth

uri = "mongodb+srv://Pawarit:PS1234@cluster0.xox3wyk.mongodb.net/?retryWrites=true&w=majority"
app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'name'
app.config['BASIC_AUTH_PASSWORD'] = 'pass'
basic_auth = BasicAuth(app)

try:
    client = MongoClient(uri)
    client.admin.command('ping')
    print("Pinged your deployment. You successfully ")
except Exception as e:
    print(e)

@app.route("/")
def Greet():
    return "<p>Welcome to Student Management API</p>"

@app.route("/students", methods =["GET"])
@basic_auth.required
def show_all_students():
    db = client["students"]
    collection = db["stu_info"]
    all_students = list(collection.find())
    return jsonify(all_students)

if __name__ == '__main__' :
    app.run(host = "0.0.0.0", port = 5000,debug = True )