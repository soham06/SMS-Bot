import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
from os import environ

load_dotenv()

api = tradeapi.REST(environ.get('APCA_API_KEY_ID'), environ.get('APCA_API_SECRET_KEY'), environ.get('APCA_API_BASE_URL'), api_version='v2')

# Get our account information.
def get_account_details():
    account = api.get_account()
    message = f"\nAccount Number: {account.account_number}\nAccount Status: {account.status}\nCash Amount: ${account.cash}\nEquity: ${account.equity}\nBuying Power: ${account.buying_power}"
    return message

def get_stock_quote(symbol):
    try:
        barset = api.get_barset(symbol, 'day', limit=1)
        price = barset[symbol][0].c
        message = f"Symbol: {symbol}\nCurrent Price: {price}"
        return(message)
    except:
        message = "Invalid Ticker Symbol. Please Try Again"
        return(message)

def post_buy_stock(ticker, quantity, order, price):
    try:
        if order == True:
            api.submit_order(
                symbol=ticker,
                qty=quantity,
                side='buy',
                type='limit',
                time_in_force='gtc',
                limit_price=float(price)
            )
            message = f"Successfully placed Market Buy Order for {quantity} {ticker} shares"
            return message
        else:
            api.submit_order(
                symbol=ticker,
                qty=quantity,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            message = f"Successfully placed Limit Buy Order for {quantity} {ticker} shares"
            return message
    except:
        message = "Unable to complete Buy Order"
        return(message)


def post_sell_stock(ticker, quantity):
    try:
        api.submit_order(
            symbol=ticker,
            qty=quantity,
            side='sell',
            type='market',
            time_in_force='gtc',
            )
        message = f"Successfully placed Sell Order for {quantity} {ticker} shares"
        return message
    except:
        message = "Unable to complete Sell Order"
        return(message)

def get_orders():
    orders = api.list_orders()
    if len(orders) == 0:
        return("You have no Orders")
    else:
        message = "\nOrder History:\n"
        count = 1
        for order in orders:
            message_per_order = f"\n{count}. Symbol: {order.symbol}, Quantity: {order.qty}, Type: {order.side}, Status: {order.status}"
            message += message_per_order
            count = count + 1
        return message

def get_positions():
    positions = api.list_positions()
    if len(positions) == 0:
        return("You have no Open Positions")
    else:
        message = "\nOpen Positions:\n"
        count = 1
        for position in positions:
            message_per_position = f"\n{count}. Symbol: {position.symbol}, Quantity: {position.qty}, Cost-Average: {position.cost_basis}, Type: {position.side}"
            message += message_per_position
            count = count + 1
        return message

def get_daily_change():
    account = api.get_account()
    change_value = float(account.equity) - float(account.last_equity)
    change_percentage = (float(change_value) / float(account.last_equity)) * 100
    message = f"\nDaily Change (in Dollars): ${round(change_value, 2)}\nDaily Change (in Percentage): {round(change_percentage, 2)}%\n"
    return message

def time_to_market_close():
    clock = api.get_clock()
    return str(clock.next_close - clock.timestamp)[7:]

def time_to_market_open():
    clock = api.get_clock()
    return str(clock.next_open - clock.timestamp)[7:]

def get_watchlist_stocks():
    watchlists = api.get_watchlist_by_name('Primary Watchlist').assets
    message = "\nStock on Current Watchlist:\n\n"
    for i in range(len(watchlists)):
        symbol = watchlists[i]['symbol']
        name = watchlists[i]['name']
        message_per_watchlist = f"{symbol}: {name}\n"
        message += message_per_watchlist
    return message

def post_add_watchlist(ticker):
    try:
        api.add_to_watchlist(environ.get('WATCHLIST_ID'), ticker)
        message = f"Successfully Added {ticker} to your Watchlist"
        return message
    except:
        message = f"Unable to Add {ticker} to your Watchlist"
        return message
        
