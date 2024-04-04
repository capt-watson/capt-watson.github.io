
from fyers_api import fyersModel
from fyers_api import accessToken
from fyers_api.Websocket import ws
from datetime import datetime, time, timedelta, date
from tradingview_ta import TA_Handler, Interval, Exchange
# import talib as ta
import pandas as pd
import document_file
import os

# pd.options.display.max_rows = 999
# pd.set_option('display.max_rows', 999)
# pd.set_option('display.max_columns', 999)
# pd.set_option('display.width', 1000)


def get_access_token():
    if not os.path.exists('access_token.txt'):
        session = accessToken.SessionModel(
        client_id=document_file.app_id,
        secret_key=document_file.secret_id,
        redirect_uri=document_file.redirect_uri,
        response_type= document_file.response_type,
        grant_type=document_file.grant_type)
        response = session.generate_authcode()
        print('login url: ', response)
        auth_code = input('Enter Auth Code: ')
        session.set_token(auth_code)
        access_token = session.generate_token()['access_token']
        with open('access_token.txt', 'w') as f:
            f.write(access_token)
    else:
        with open('access_token.txt', 'r') as f:
            access_token = f.read()
    return access_token

fyers = fyersModel.FyersModel(client_id=document_file.app_id, token=get_access_token(),is_async=False,log_path=document_file.log_path)

## Historical Data 

data = {'symbol': 'NSE:SBIN-EQ',
        'resolution': '1',
        'date_format':1,
        'range_from':'2024-3-1',
        'range_to': '2024-3-3',
        'cont_flag':'1'
        }
    
hist = fyers.history(data=data)

for value in hist.values():
    for list in value:
        print(list)

# # print(hist)



## Quotes 

# data = {'symbols':'NSE:HDFCBANK-EQ'}
# res = fyers.quotes(data=data)

# print(res)




## Market Depth 

# data = {"symbol":"NSE:SBIN-EQ","ohlcv_flag":"1"}
# print(fyers.depth(data),'\n')


# #1. User Apis : This includes (Profile,Funds,Holdings)

# print(fyers.get_profile(),'\n') ## This will provide us with the user related data 

# print(fyers.funds(),'\n')      ## This will provide us with the funds the user has 

# print(fyers.holdings(),'\n')   ## This will provide the available holdings the user has

# print(fyers.tradebook(),'\n')  ## This will provide all the trade related information 

# print(fyers.orderbook(),'\n')  ## This will provide the user with all the order related information 

# print(fyers.positions(),'\n')  ## This will provide the user with all the positions the user has on his end



# # SINGLE ORDER 

# data =  {
#       "symbol":"NSE:ONGC-EQ",
#       "qty":1,
#       "type":1,
#       "side":1,
#       "productType":"INTRADAY",
#       "limitPrice":0,
#       "stopPrice":0,
#       "validity":"DAY",
#       "disclosedQty":0,
#       "offlineOrder":"False",
#       "stopLoss":0,
#       "takeProfit":0
#     }                    

# ## This is a sample example to place a limit order you can make the further changes based on your requirements 

# print(fyers.place_order(data))


# ## MULTI ORDER 

# data = [{ "symbol":"NSE:SBIN-EQ",
#   "qty":1,
#   "type":1,  
#   "side":1, 
#   "productType":"INTRADAY",   
#   "limitPrice":61050,
#   "stopPrice":0 ,
#   "disclosedQty":0, 
#   "validity":"DAY", 
#   "offlineOrder":"False", 
#   "stopLoss":0,  
#   "takeProfit":0
# },
# {
#   "symbol":"NSE:HDFC-EQ",
#   "qty":1,
#   "type":2,  
#   "side":1, 
#   "productType":"INTRADAY",   
#   "limitPrice":0,
#   "stopPrice":0 ,
#   "disclosedQty":0, 
#   "validity":"DAY", 
#   "offlineOrder":"False", 
#   "stopLoss":0,  
#   "takeProfit":0
# }]                

# ### This takes input as a list containing multiple single order data into it and the execution of the orders goes in the same format as mentioned.

# print(fyers.place_basket_orders(data))



#4. Other Transaction : This includes (modify_order,exit_position,cancel_order,convert_positions)

# ## Modify_order request 
# data = {
#           "id":7574657627567, 
#           "type":1, 
#           "limitPrice": 61049,
#           "qty":1
#       }

# print(fyers.modify_order(data))


# ## Modify Multi Order 

# data = [
#     { "id":8102710298291,
#   "type":1,
#   "limitPrice": 61049,
#   "qty":0
# },
# {
#   "id":8102710298292,
#   "type":1,
#   "limitPrice": 61049,
#   "qty":1 
# }]

# print(fyers.modify_basket_orders(data))



# ### Cancel_order

# data = {"id":'808058117761'}
# print(fyers.cancel_order(data))



# ### cancel_multi_order 
# data  =  [
# { 
#    "id":'808058117761'
#  },
#  {
#    "id":'808058117762'
#  }]
 
# print(fyers.cancel_basket_orders(data))



# ### Exit Position

# data  = {
#      "id":"NSE:SBIN-EQ-INTRADAY"
#    }

# print(fyers.exit_positions(data))



# ### Convert Position

# data = {
#      "symbol":"MCX:SILVERMIC20NOVFUT",
#      "positionSide":1,
#      "convertQty":1,
#      "convertFrom":"INTRADAY",
#      "convertTo":"CNC"
#    }

# print(fyers.convert_position(data))

# exchange = 'NSE'
# quantity = int(100)
# timeframe = '5'
# from_date = '2024-01-01'
# today = datetime.datetime.now().strftime('%Y-$m-%d')
# rsi_overbought = 80
# rsi_oversold = 20
# buy_traded_stock = []
# sell_traded_stock = []

# open_position = []


# script_list = ['HDFCBANK-EQ','SBIN-EQ','INFY-EQ', 'AXISBANK-EQ', 'MARUTI-EQ']


# def getTime():
#     return datetime.datetime.now().strftime('%Y-%m-%d %i:%M:%S')

# def placeOrder(script, order):
#     if order == 'BUY':
#         order = fyers.place_order({'symbol':f'{exchange}:{script}','qty':quantity, 'type':'2', 'side':'1', 'productType':'INTRADAY'})

# def rsiAlgorithm():
#     for script in script_list:
#         data = {'symbol':f'{exchange}:{script}','resolution':timeframe, 'date_format':'1','range_from':from_date, 'range_to':today}
#     try:
#         hist_data = fyers.history(data)
#     except Exception as e:
#         raise e
#     df = pd.DataFrame(hist_data['candles'],columns = ['date','open','high','low','close','volume'])
#     df['date'] = pd.to_datetime(df['date'],unit='s',utc=True)
#     df['date'] = df['date'].dt.tz_convert('Asia/Kolkata')
#     df['rsi'] = ta.RSI(df['close'],timeperiod=14).round(2)
#     df.dropna(inplace=True)
#     if not dt.empty():
#         rsi_value = df.rsi.values[-1]
#         #print(df)
#         if(rsi_value >= rsi_overbought) and (script not in sell_traded_stock):
#             sell_traded_stock.append(script)
#             placeOrder(script, 'SELL')

#         if(rsi_value <= rsi_oversold) and (script not in buy_traded_stock):
#             buy_traded_stock.append(script)
#             placeOrder(script,'BUY')
            
# def main():
#     global fyers
    
#     auth_code = generate-auth_code()
#     access_token = generate_access_token(auth_code, client_id, secret_key)
#     fyersModel = fyersModel.FyersModel(token=access_token, log_path= log_path, client_id=client_id)
#     fyers.token = access_token
    
#     closingtime = int(15)*60+int(10)
#     orderplacetime = int(9)*60+int(10)
#     timenow = (datetime.datetime.now().hour*60 + datetime.datetime.now().minute)
#     print(f'Waiting for 9:20 AM, Time Now:{getTime()}')
    
#     while timenow < orderplacetime:
#         time.sleep(0.2)
#         timenow = (datetime.datetime.now().hour*60 + datetime.datetime.now().minute)
#         print(f'Ready for Trading, Time Now:{getTime()}')
        
#     while timenow < closingtime:
#         rsiAlgorithm()
        
# if __name__ == '__main__':
#     main()

#DATA APIS : This includes following Apis(History,Quotes,MarketDepth)

symbols = ['GESHIP','SBIN','HDFCBANK','HAL','BEL','ADANIGREEN','MAZDOCK']

# for symbol in symbols:
#     output = TA_Handler(symbol= symbol,
#     screener = 'india',
#     exchange='NSE',
#     interval=Interval.INTERVAL_5_MINUTES)
#     print('Symbol: '+symbol)
#     print(output.get_analysis().summary,'\n')
#     # print(pd.DataFrame(output.get_analysis().indicators))
    