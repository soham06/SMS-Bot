greeting_message = '''\nGreetings Investor! My name is Stockie, your one stop shop to trade stocks! For a complete list of all my commands, enter !commands and press enter. Good Luck and Happy Trading!'''

commands_list = '''\nDisclaimer: Make sure you follow the command structure accurately to avoid any errors! As well, there is no need to enter brackets when entering commands, however make sure to adhere to the appropriate space count!\n\nComplete List of Commands:\n
!commands - returns a complete list of Stockie's commands\n
!account - returns equity, buying power, balance and other details about your account\n
!quote [stock symbol] - returns the current price of the stock\n
!buy [stock symbol] [quantity] [limit] [limit price] - buys quantity amount of stocks (only put limit if you want a limit order and if so put limit price as well!)\n
!sell [stock symbol] [quantity] - sells quantity amount of stocks (only put limit if you want a limit order and if so put limit price as well!)\n
!positions - returns all open positions in account\n
!orders - returns all open orders in account\n
!change - returns the daily change in account value\n
!watchlist get - returns you current stock watchlist\n
!watchlist add [stock symbol] - adds the stock to your watchlist\n
!timeopen - returns time till market open\n
!timeclose - returns time till market close\n'''

invalid_command = "\nInvalid Command. Enter !commands to get a full list of my commands!\n"
