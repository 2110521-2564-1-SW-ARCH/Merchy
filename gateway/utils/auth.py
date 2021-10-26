import jwt,os

def verify_token(token):
    try:
        decoded = jwt.decode(token, os.getenv('SECRET'),"HS256")
        if decoded: return decoded
        else: return False
    except:
        return False
