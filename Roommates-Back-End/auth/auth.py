from flask_jwt_extended import create_access_token
from datetime import timedelta
from database.auth.dao import AuthDao



def login(username, password,):

    dao = AuthDao()
    user = dao.login(username, password)

    if user:
        # Tiempo que tarda en expirar el token
        expires_in = timedelta(seconds=15)
        # Creacion del token, identity se espera que sea el identificador unico del usuario,
        print(user)

        claims = {'role': 'user', 'mail': user.get('mail'), 'id': user.get('id')}
        access_token = create_access_token(identity=username,
                                           fresh=True, expires_delta=expires_in,
                                           additional_claims=claims)
        return access_token, 200
    else:
        return {"msg": "Credenciales inválidas"}, 401
