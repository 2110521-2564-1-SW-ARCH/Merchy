from django.http.response import JsonResponse
from functools import wraps
from utils.auth import verify_token
def jwt_verified(methods):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.method in methods:
                if request.decoded_user: return view_func(request, *args, **kwargs)
                else: return JsonResponse({"message": "Unauthorized"})
            else: return view_func(request, *args, **kwargs)
        return wrapper
    return decorator