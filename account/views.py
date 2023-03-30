from rest_framework.response import Response
from rest_framework import status
from .database import collection
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from . utils import get


@csrf_exempt
@api_view(['GET', ])
def GetAccountInfo(request):
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
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', ])
def get_account_info_single(request, login):
    if request.method == 'GET':
        result = collection.find({'login': login}).sort('date', -1)
        x = get(result)
        data = [x]
        return Response(data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)