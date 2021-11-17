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
