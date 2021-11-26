import json
import threading
from time import sleep
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from accounting.amqp import produce, consume
from utils.decorators import jwt_verified

response = None


def fill_response(ch, method, properties, body):
    global response
    response = json.loads(body.decode())


def wait_for_response(timeout=5):
    time = 0
    while response == None:
        if time > timeout:
            break
        time += 0.5
        sleep(0.5)

consumer_thread = threading.Thread(target=lambda: consume(fill_response))
consumer_thread.start()


# Create your views here.
@api_view(["GET"])
@jwt_verified(["GET"])
def getSales(request):
    user_id = request.decoded_user["id"]
    if request.method == 'GET':
        global response
        response = None
        msg = {
            "resourceType": request.GET.get("resourceType"),
            "startDate": request.GET.get("startDate"),
            "endDate": request.GET.get("endDate"),
            "scale": request.GET.get("scale"),
            "userId": user_id
        }

        produce(msg)
        wait_for_response()

        return JsonResponse(response, safe=False) if response != None else HttpResponse("JSON please")
