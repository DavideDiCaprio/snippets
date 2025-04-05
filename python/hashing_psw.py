import bcrypt 

password = b'latupa'
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password=password, salt=salt)
print(f'Hashed psw = {hashed.decode("utf-8")}')



'''
pip install bcrypt
'''