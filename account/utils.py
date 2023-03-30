import threading
import MetaTrader5 as MT5Terminal
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


# define a list of account credentials
accounts = [{'login': 51135132, 'password': 'yym2fmut', 'server': 'ICMarketsEU-Demo'},
            {'login': 51135134, 'password': 'u5qoleim', 'server':'ICMarketsEU-Demo'},
            {'login': 22014542, 'password': 'duzftxd8', 'server': 'Deriv - Demo'}]


# define a function to retrieve equity and balance for an account
def get_equity_balance():
    # connect to the MetaTrader 5 API server
    #   q.put(account)
    for acct in accounts:
        if not MT5Terminal.initialize():
            print("initialize() failed")
            return
        if not MT5Terminal.login(login=acct['login'], password=acct['password'], server=acct['server'], timeout=60000):
            print(f"login({acct['login']}) failed")
            return

    # retrieve the equity and balance for the account
    account_info = MT5Terminal.account_info()
    equity = account_info.equity
    balance = account_info.balance
    login = account_info.login
    leverage = account_info.leverage
    currency = account_info.currency

    # print the equity and balance for the account
    print(
        f"Account {login}: Equity = {equity}, Balance = {balance}, Login = {login}, leverage = {leverage}", )

    # disconnect from the MetaTrader 5 API server
    #   MT5Terminal.shutdown()
    return login, equity, balance, leverage, currency


#   q = Queue()
#   login=, password=, server=

def get_data():
    t1 = threading.Thread(target=get_equity_balance, args=(22014542, 'duzftxd8', 'Deriv-Demo'))
    t2 = threading.Thread(target=get_equity_balance, args=(51135132, 'yym2fmut', 'ICMarketsEU-Demo'))
    t1.start()
    t1.join()
    t2.start()
    t2.join()
