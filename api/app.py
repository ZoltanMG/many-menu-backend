import models
from crypt import methods
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    return "index"


@app.route('/recetas', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/recetas/<text>', strict_slashes=False)
def recetas(text):
    return "text: {}".format(text)

#####


@app.route('/login', methods=['GET'])
def login():
    return jsonify({'response': 'login'})

@app.route('/signup', methods=['GET'])
def signup():
    return jsonify({'response': 'signup'})

@app.route('/mis-recetas', methods=['GET'])
def mis_recetas():
    recetasCard = [
    {
        "id": 1,
        "nombreReceta": "Arroz blanco",
        "favorito": False,
        "colorCard": "tomato"
    },
    {
        "id": 2,
        "nombreReceta": "Cazuela de marizcos en salsa de ajo",
        "favorito": False,
        "colorCard": "tomato"
    },
    {
        "id": 3,
        "nombreReceta": "Ceviche",
        "favorito": True,
        "colorCard": "tomato"
    }
]
    return jsonify(recetasCard)


@app.after_request
def after(response):
    response.headers["Access-Control-Allow-Origin"] = '*'
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return(response)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=4000,
        debug=True,
        threaded=True
    )