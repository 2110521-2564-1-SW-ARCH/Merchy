import json
import threading
from time import sleep
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from accounting.amqp import produce, consume

response = None


def fill_response(ch, method, properties, body):
    global response
    response = json.loads(body.decode())


def _consume(queue, cb, timeout=2):
    global response

    consumer_thread = threading.Thread(target=lambda: consume("response", cb))
    consumer_thread.start()
    time = 0
    while response == None:
        if time > timeout:
            break
        time += 0.5
        sleep(0.5)
    consumer_thread.join(timeout=0.1)


# Create your views here.
@api_view(["GET", "POST", "DELETE"])
def getSales(request):
    global response
    msg = {
        "resourceType": request.GET.get("resourceType"),
        "startDate": request.GET.get("startDate"),
        "endDate": request.GET.get("endDate"),
        "scale": request.GET.get("scale"),
    }

    produce("request", msg)
    _consume("response", fill_response)
    
    return JsonResponse(response, safe=False) if response != None else HttpResponse("JSON please")
