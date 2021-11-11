from utils.auth import verify_token

def AttachUserMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        token = request.COOKIES.get('token')
        user = verify_token(token)
        if user: request.decoded_user = user
        else : request.decoded_user = False

        response = get_response(request)

        return response
    return middleware