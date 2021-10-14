from flask import Flask, request, jsonify
from data import data

app = Flask(__name__)
@app.route("/")

def display():
    return jsonify({
        "Final_data":data,
        "message":"success"
    }), 200

@app.route("/language")
def query():
    language = request.args["program"]
    framework = request.args.get("framework")
    return '''<h1> "The program method is {}" </h1>
              <h1> The framework name is {} <h1> 
    '''.format(language, framework)

@app.route("/planets")
def planets():
    querryname = request.args.get("name")
    planetData = next(i for i in data if i["name"] == querryname)
    return jsonify({
            "data":planetData, 
            "message":"success",

        }),200





if __name__ == "__main__":
    app.run(debug = True, host = "localhost")

