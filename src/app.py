from crypt import methods
from flask import Flask, jsonify
from data import users

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'response': 'hello Wolrd'})

@app.route('/users', methods=['GET'])
def usersHandler():
    return jsonify({'users': users})


@app.after_request
def after(response):
    """
    Esta función verifica la sesión después de una solicitud y
    le da al CORS con la interfaz que permite la conexión
    entre la parte posterior y la frontal.
    """
    # response.headers["Access-Control-Allow-Origin"] = '*' todos los lugares
    response.headers["Access-Control-Allow-Origin"] = 'http://localhost:3000'
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=4000, debug=True) todos los lugares
    app.run(port=4000, debug=True)