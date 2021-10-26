import requests

def create_requests_with_header(request):
    r = requests.Session()
    token = request.COOKIES.get('token')
    r.cookies.set('token', token)
    return r