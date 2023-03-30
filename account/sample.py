import MetaTrader5 as mt5
import pymongo
from datetime import datetime, timedelta

client = pymongo.MongoClient("mongodb+srv://welzatm:Mayflower48@cluster0.9efveyx.mongodb.net/?retryWrites=true&w"
                             "=majority")
#   db = client['FT9JA']
db = client['NewFT9JA']
collection = db['AccountInfo']

# connect to MetaTrader5 platform
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()


def get_all_symbols(symbols):
    now = datetime.now()
    start_time = now - timedelta(hours=1)
    end_time = now
    #   symbols = mt5.symbols_get()
    market = []
    for sym in symbols:
        market_date = mt5.copy_rates_range(sym, mt5.TIMEFRAME_H1, start_time, end_time)
        for mkt in market_date:
            market.append(mkt)
            print(mkt)

    return market

# authenticate with account details
login = 51135132
password = "yym2fmut"
server = 'ICMarketsEU-Demo'

authorized = mt5.login(login, password, server, timeout=60000)
if authorized:
    print("connected to account #", login)
else:
    print("failed to connect at account #{}, error code: {}".format(login, mt5.last_error()))
    quit()


def get_data():
    # get Equity and Balance
    account_info = mt5.account_info()
    symbols = mt5.symbols_total()
    equity = account_info.equity
    balance = account_info.balance
    liabilities = account_info.liabilities
    login = account_info.login
    currency = account_info.currency
    leverage = account_info.leverage
    date_pulled = datetime.now()  # to enable sorting my time

    # get Market Watch Time
    #   time_info = mt5.market_watch_time("EURUSD")
    #   market_watch_time = time_info.time_msc

    return login, equity, balance, liabilities, currency, leverage, date_pulled


# schedule function to run at 1-minute intervals
while True:
    login, equity, balance, liabilities, currency, leverage, ddate = get_data()
    #   time = datetime.now()
    collection.insert_one({
        'date': ddate,
        'login': login,
        'equity': equity,
        'balance': balance,
        'liabilities': liabilities,
        'currency': currency,
        'leverage': leverage,
    })

    #   Use Celery and create this script for server 2 and 3
