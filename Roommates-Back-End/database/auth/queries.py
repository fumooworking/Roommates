CHECK_CREDENCIALS = """
SELECT * FROM user 
WHERE username=%s 
AND password=%s
"""

REGISTER = """
INSERT INTO user (username, mail, password) 
VALUES (%s, %s, %s)
"""