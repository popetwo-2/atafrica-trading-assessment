from rest_framework.response import Response
from rest_framework import status
from .database import collection
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from . utils import get
from django.shortcuts import render


def home(request):
    if request.method == 'GET':
        #   result = collection.find().sort('date', -1)
        result1 = collection.find({'login': 22014542}).sort('date', -1)
        result2 = collection.find({'login': 51135134}).sort('date', -1)
        result3 = collection.find({'login': 51135132}).sort('date', -1)

        x = get(result1)
        y = get(result2)
        z = get(result3)
        res = {
            '22014542': [x],
            '51135134': [y],
            '51135132': [z]
        }
        context = {
            '1': {'equity': res['22014542'][0]['equity'], 'balance': res['22014542'][0]['balance'], 'login': res['22014542'][0]['login']},
            '2': {'equity': res['51135134'][0]['equity'], 'balance': res['51135134'][0]['balance'], 'login': res['51135134'][0]['login']},
            '3': {'equity': res['51135132'][0]['equity'], 'balance': res['51135132'][0]['balance'], 'login': res['51135132'][0]['login']}
        }
        return render(request, 'home.html', context)


@csrf_exempt
@api_view(['GET', ])
def GetAccountInfo(request):
    if request.method == 'GET':
        result = collection.find().sort('date', -1)
        result1 = collection.find({'login': 22014542}).sort('date', -1)
        result2 = collection.find({'login': 51135134}).sort('date', -1)
        result3 = collection.find({'login': 51135132}).sort('date', -1)

        x = get(result1)
        y = get(result2)
        z = get(result3)
        data = []
        for res1 in result:
            data.append({
                'date': res1['date'],
                'login': res1['login'],
                'equity': res1['equity'],
                'leverage': res1['leverage'],
                'balance': res1['balance'],
                'currency': res1['currency']
            })

        res = {
            '22014542': [x],
            '51135134': [y],
            '51135132': [z]
        }
        data1 = [{
            '1': {'equity': res['22014542'][0]['equity'], 'balance': res['22014542'][0]['balance']},
            '2': {'equity': res['22014542'][0]['equity'], 'balance': res['22014542'][0]['balance']},
            '3': {'equity': res['22014542'][0]['equity'], 'balance': res['22014542'][0]['balance']}
        }]
        return Response(data1, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


def dashboard(request):
    if request.method == 'GET':
        result = collection.find().sort('date', -1)
        data = []
        for res in result:
            data.append({
                'date': res['date'],
                'login': res['login'],
                'equity': res['equity'],
                'leverage': res['leverage'],
                'balance': res['balance'],
                'currency': res['currency']
            })
        context = {
            'data': data
        }
        return render(request, 'dashboard.html', context)



@csrf_exempt
@api_view(['GET', ])
def get_account_info_single(request, login):
    if request.method == 'GET':
        result = collection.find({'login': login}).sort('date', -1)
        x = get(result)
        data = [x]
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
def challenge(request):
    return render(request, 'challenge.html', {})