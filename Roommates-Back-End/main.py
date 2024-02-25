from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
CORS(app, supports_credentials=True, origins=['http://localhost:3000'])
# Configuración del JWT
app.config['JWT_SECRET_KEY'] = 'roommates'  # Cambiar esto con una clave secreta segura
jwt = JWTManager(app)


@app.route('/')
@cross_origin()
@app.errorhandler(404)
def not_found_error(error):
    return error + '404'


if __name__ == '__main__':
    app.run()
