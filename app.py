
from flask import Flask, jsonify, request


app = Flask(__name__)



# Route to get all items
@app.route('/', methods=['GET'])
def get_items():
    print("hello")
    return jsonify({"id": 1, "name": "Item 1"})

@app.route('/yourname', methods=['GET'])
def get_name():
    print("hello")
    return "Nitin Singh"



if __name__ == '__main__':
    app.run(port=1234,debug=True)



