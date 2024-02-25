# Eliminar usuario por id
DELETE_USER_BY_ID = """
DELETE FROM user 
WHERE id = %s
"""

# Modificar usuario por id
PATCH_USER_BY_ID = """
UPDATE user
SET
  username = COALESCE(%s, username),
  mail = COALESCE(%s, mail),
  password = COALESCE(%s, password)
WHERE id = %s;
"""

# Visualizar los datos de un usuario en concreto por id
GET_USER_BY_ID = """
SELECT * FROM user WHERE user.id = %s;
"""

# Visualizar los datos de un usuario en concreto por username
GET_USER_BY_USERNAME = """
SELECT * FROM user WHERE user.username = %s;
"""

