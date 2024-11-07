from flask import Flask, request, jsonify


users = {
    1: {
        "name": "Alex",
        "age": 28
    },
    
    2: {
        "name": "Max",
        "age": 28
    },
    3: {
        "name": "Jesus",
        "age": 2029
    }
}
app = Flask(__name__)
@app.route('/hello_world', methods=['GET'])
def sayHelloWorld():
    
    data = {
        1: "Hiiiiiii"
    }
    return jsonify(data)

@app.route('/users/', methods=['GET'])
def retunUserInfo():
    id = int(request.args.get("id") )   
    if (id<= 0 or id >= 3):
        return jsonify("invalid value")
    return jsonify(users[id])



if __name__ == "__main__":
    app.run(debug=True)
