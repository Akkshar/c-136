from flask import Flask, request, jsonify
from Star_data import my_object

app = Flask(__name__)
@app.route("/")

def display():
    return jsonify({
        "Final_data":my_object,
        "message":"success"
    }), 200

@app.route("/stars")
def Stars():
    query = request.args.get("name")
    star_data = next(i for i in my_object if i["Name"] == query)
    return jsonify ({
        "star_data":star_data, 
        "message":"success"
    }), 200

if __name__ == "__main__":
    app.run(debug = True, host = "localhost")