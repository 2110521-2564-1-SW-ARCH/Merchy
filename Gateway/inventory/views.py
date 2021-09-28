from django.shortcuts import render, redirect
from .forms import EntryForm
from datetime import datetime

#  for grpc
import grpc
import merchy_pb2
import merchy_pb2_grpc
from google.protobuf.json_format import MessageToDict

channel = grpc.insecure_channel('0.0.0.0:3001') # should be closed by channel.close()
stub = merchy_pb2_grpc.InventoryServiceStub(channel)

mockup_entries = [
    {'id': 0, 'name': 'Food', 'price': 100, 'amount': 3, 'time': '26/09/2021 20:00', 'note': 'KFC' },
    {'id': 1, 'name': 'Cat', 'price': 500, 'amount': 1, 'time': '27/09/2021 09:00', 'note': 'Persian' },
    {'id': 2, 'name': 'Collar', 'price': 35, 'amount': 1, 'time': '27/09/2021 12:00', 'note': 'Red' },
]


def convertTime(time_string):
    time_string = time_string.split(' (')[0]
    return datetime.strptime(time_string, "%a %b %d %Y %H:%M:%S GMT%z")


# Create your views here.
def render_inventory(request):
    if (request.method == 'GET'):
        response = stub.GetAllEntries(merchy_pb2.Empty())
        entries = response.entries
        return render(request, 'inventory/index.html', {'entries': entries})
    elif (request.method == 'POST'):
        print('YAY')


def render_entry(request, entry_id):
    if (request.method == 'GET'):
        entry = stub.Get(merchy_pb2.EntryId(id=entry_id))
        entry = MessageToDict(entry)
        entry['time'] = convertTime(entry['time'])
        return render(request, 'inventory/entry.html', entry)
    elif (request.method == 'POST'):
        data = request.POST
        form = EntryForm(data)
        if form.is_valid():
            createdEntry = stub.Insert(merchy_pb2.Entry(
                item={
                    "id": "6151dbd75d645ab4e25b14c8"
                },
                price=data['price'],
                amount=data['amount'],
                note=data['note'],
                time=str(datetime.now())
            ))
            print(data['name'])
        return redirect(f'/inventory/{entry_id}')


def update_entry(request):
    return render(request, 'inventory/index.html')


def delete_entry(request):
    return render(request, 'inventory/index.html')
