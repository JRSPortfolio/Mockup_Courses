all = ('set_auth_cookie',
       'get_auth_from_cookie',
       'delete_auth_cookie',
       'hash_cookie_value',
       'get_current_user',
       'requires_unauthentication')

from hashlib import sha512

from database import database_crud as db_c
from fastapi import HTTPException, Request, Response, status
from infrastructure.middleware import global_request

AUTH_COOKIE_NAME = 'user_id'
SECRET_KEY = '8e10a458e68dff54488dds5588d69984vf488ry5588c1236d66'

def set_auth_cookie(response: Response, user_id: int):
    cookie_value = f'{user_id}:{hash_cookie_value(str(user_id))}'
    response.set_cookie(AUTH_COOKIE_NAME,
                        cookie_value,
                        secure = False,
                        httponly = True,
                        samesite = 'lax')
    
def get_auth_from_cookie(request: Request):
    if not (cookie_value := request.cookies.get(AUTH_COOKIE_NAME)):
        return None
    
    parts = cookie_value.split(':')
    if len(parts) != 2:
        return None
    
    user_id, hash_value = parts
    hash_value_check = hash_cookie_value(user_id)
    if hash_value != hash_value_check:
        print('Valor de cookie inválido!')
        return None
    
    return int(user_id) if user_id.isdigit() else None

def delete_auth_cookie(response: Response):
    response.delete_cookie(AUTH_COOKIE_NAME)

def hash_cookie_value(value :str):
    return sha512(f'{value}{SECRET_KEY}'.encode('utf-8')).hexdigest()

def get_current_user():
    if student_id := get_auth_from_cookie(global_request.get()):
        return db_c.get_db_student_by_id(student_id)
    return None
    
def requires_unauthentication():
    if get_current_user():
        raise HTTPUnauthorizedOnly(detail = 'This is a public area only.')
    
def requires_authentication():
    if not get_current_user():
        raise HTTPUnauthorizedAccess(detail = 'This area requires authentication.')
    
class HTTPUnauthorizedAccess(HTTPException):
    def __init__(self, *args, **kargs):
        super().__init__(status_code = status.HTTP_401_UNAUTHORIZED, *args, **kargs)

class HTTPUnauthorizedOnly(HTTPUnauthorizedAccess):
    ...
        

