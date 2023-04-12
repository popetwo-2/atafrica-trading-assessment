import threading
#   import MetaTrader5 as MT5Terminal
import time
from multiprocessing.pool import ThreadPool


def get(results):
    data = []
    for res in results:
        data.append({
            'date': res['date'],
            'login': res['login'],
            'equity': res['equity'],
            'leverage': res['leverage'],
            'balance': res['balance'],
            'currency': res['currency']
        })
    return data[-1]
