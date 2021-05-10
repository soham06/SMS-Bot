from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import commands
from alpaca import *

app = Flask(__name__)

# application routes
@app.route("/")
def index():
  return "Welcome to Stockie"

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    greeting_commands = ["hey", "hello", "hi"]
    message_body = request.form['Body']
    resp = MessagingResponse()

    if message_body.lower() in greeting_commands:
        body_response = greeting()
        resp.message(body_response)
    elif message_body[0] == '!':
        message_body = message_body[1:]
        message_body = message_body.split(' ')
        if message_body[0].lower() == "commands":
            body_response = command_list()
            resp.message(body_response)
        elif message_body[0].lower() == "account":
            body_response = account_details()
            resp.message(body_response)
        elif message_body[0].lower() == "quote":
            body_response = stock_quote(message_body[1].upper())
            resp.message(body_response)
        elif message_body[0].lower() == "buy":
            if len(message_body) > 3:
                if message_body[3] == 'limit':
                    body_response = buy_stock(message_body[1], message_body[2], True, message_body[4])
                    resp.message(body_response)
            else:
                body_response = buy_stock(message_body[1], message_body[2], False, 0)
                resp.message(body_response)
        elif message_body[0].lower() == "sell":
            body_response = sell_stock(message_body[1], message_body[2])
            resp.message(body_response)
        elif message_body[0].lower() == "positions":
            body_response = positions_list()
            resp.message(body_response)
        elif message_body[0].lower() == "orders":
            body_response = orders_list()
            resp.message(body_response)
        elif message_body[0].lower() == "change":
            body_response = daily_change()
            resp.message(body_response)
        elif message_body[0].lower() == "timeopen":
            body_response = open_time()
            resp.message(f"Market Opens in: {body_response}")
        elif message_body[0].lower() == "timeclose":
            body_response = close_time()
            resp.message(f"Market Closes in: {body_response}")
        elif message_body[0].lower() == "watchlist":
            if message_body[1].lower() == "get":   
                body_response = watchlist_get()
                resp.message(body_response)
            elif message_body[1] == "add":
                body_response = watchlist_add(message_body[2])
                resp.message(body_response)
            else:
                resp.message(commands.invalid_command)
        else:
                resp.message(commands.invalid_command)             
    else:
        resp.message(commands.invalid_command)

    return str(resp)

def greeting():
    return commands.greeting_message

def command_list():
    return commands.commands_list

def account_details():
    return get_account_details()

def stock_quote(symbol):
    return get_stock_quote(symbol)

def buy_stock(symbol, qty, limit, limit_price):
    return post_buy_stock(symbol, int(qty), limit, limit_price)

def sell_stock(symbol, qty):
    print(symbol)
    print(qty)
    return post_sell_stock(symbol, int(qty))

def positions_list():
    return get_positions()

def orders_list():
    return get_orders()

def daily_change():
    return get_daily_change()

def watchlist_get():
    return get_watchlist_stocks()

def watchlist_add(symbol):
    return post_add_watchlist(symbol)

def open_time():
    return time_to_market_open()

def close_time():
    return time_to_market_close()

if __name__ == "__main__":
    app.run(debug=True)