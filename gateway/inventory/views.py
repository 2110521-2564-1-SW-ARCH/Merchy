from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EntryForm
from datetime import datetime

#  for grpc
import grpc
import merchy_pb2
import merchy_pb2_grpc
from google.protobuf.json_format import MessageToDict

channel = grpc.insecure_channel('127.0.0.1:3002') # should be closed by channel.close()
stub = merchy_pb2_grpc.InventoryServiceStub(channel)

mockup_entries = [
    {'id': 0, 'name': 'Food', 'price': 100, 'amount': 3, 'time': '26/09/2021 20:00', 'note': 'KFC' },
    {'id': 1, 'name': 'Cat', 'price': 500, 'amount': 1, 'time': '27/09/2021 09:00', 'note': 'Persian' },
    {'id': 2, 'name': 'Collar', 'price': 35, 'amount': 1, 'time': '27/09/2021 12:00', 'note': 'Red' },
]


# Create your views here.
def render_inventory(request):
    if (request.method == 'GET'):
        entries = stub.GetAllEntries(merchy_pb2.Empty()).entries
        items = stub.GetAllItems(merchy_pb2.Empty()).items
        return render(request, 'inventory/index.html', {'entries': entries, 'items': items})
    elif (request.method == 'POST'):
        print('YAY')


# render an entry
def render_entry(request, entry_id):
    entry = stub.GetEntry(merchy_pb2.EntryId(id=entry_id))
    entry = MessageToDict(entry)
    items = stub.GetAllItems(merchy_pb2.Empty()).items
    return render(request, 'inventory/entry.html', {'entry': entry, 'items': items})


def create_entry(request):
    if(request.method == 'POST'):
        data = request.POST
        createdEntry = stub.CreateEntry(merchy_pb2.Entry(
            item={
                "id": data['item']
            },
            price=float(data['price']),
            amount=int(data['amount']),
            note=data['note'],
            date=data['date']
        ))
        return redirect('/inventory')


def update_entry(request):
    if(request.method == 'POST'):
        data = request.POST
        updatedEntry = stub.UpdateEntry(merchy_pb2.Entry(
            id=data['id'],
            price=float(data['price']),
            amount=int(data['amount']),
            date=data['date'],
            note=data['note']
        ))
        return redirect(f'/inventory/{data["id"]}')


def delete_entry(request):
    data = request.POST
    stub.DeleteEntry(merchy_pb2.EntryId(id=data['id']))
    return redirect('/inventory')


def get_item(request):
    return HttpResponse('get item')


def get_items(request):
    if(request.method == 'GET'):
        items = stub.GetAllItems(merchy_pb2.Empty())
        return HttpResponse(items)
    return HttpResponse('get items')


def create_item(request):
    if(request.method == 'POST'):
        created_item = stub.CreateItem(merchy_pb2.Item(
            name=request.POST['name'],
            description=request.POST['description']
        ))
        return redirect('/inventory')
    return HttpResponse('create item')


def update_item(request):
    return HttpResponse('update item')


def delete_item(request):
    return HttpResponse('delete item')