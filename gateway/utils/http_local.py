import requests

def create_requests_with_header(request):
    r = requests.Session()
    token = request.COOKIES.get('token')
    r.cookies.set('token', token)
    return r

def create_session(token=''):
    r = requests.Session()
    # r.cookies.set('token', token)
    return r

class AuthService:
    def __init__(self):
        self.r = create_session()

    def get_all_user(self):
        data = self.r.get(f'http://localhost:3001/api/user').json()
        return data

    def get_one_user(self, id):
        data = self.r.get(f'http://localhost:3001/api/user/{id}').json()
        return data

    def create_user(self, data):
        created_user = self.r.post('http://localhost:3001/api/user',data=data).json()
        return created_user
        
    def delete_user(self, id):
        data = self.r.delete(f'http://localhost:3001/api/user/{id}').json()
        return data

    def update_user(self, id, data):
        updated_user = self.r.put(f'http://localhost:3001/api/user/{id}', data=data).json()
        return updated_user

    def login(self, credential):
        data = self.r.post('http://localhost:3001/api/login', data=credential)
        return data
        
