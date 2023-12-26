import json
import pyotp
import requests
import pandas as pd
from logzero import logger
from datetime import datetime
from bs4 import BeautifulSoup as bs
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
#
from SmartApi import SmartConnect  # or from smartapi.smartConnect import SmartConnect
import pyotp, time, pytz
from datetime import datetime, timedelta
import pandas as pd

#




url = "https://chartink.com/screener/process"
import os
name = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
filename = os.path.join("D:\codes",name )


# # filename = name +'.txt'

# condition  = {"scan_clause": "( {cash} ( [0] 15 minute close > 4000 and [0] 15 minute close > 1 day ago close * 1.01 and latest volume > 0 ) ) "}
condition = {"scan_clause:" "( {33489} ( [=2] 15 minute low < [=1] 15 minute low and [0] 15 minute volume > [=2] 15 minute volume and( latest low - latest high ) < ( 1 day ago low - 1 day ago high ) and 1 day ago volume > 10000 and latest rsi( 14 ) < 1 day ago rsi( 14 ) and latest rsi( 14 ) < 2 days ago rsi( 14 ) and latest ichimoku span b( 9,26,52 ) < latest ichimoku span a( 9,26,52 ) and latest low < 1 day ago low and latest low < 2 days ago low ) ) "}

# User Name: PNPT1158 Pin: 1598 Api Key: 3JhtnRvF ,token = "FZ7F2L2AYUGDWPR4YBSSBYTU7Q"
##################Angle Brokering################

# obj = SmartConnect(api_key="3JhtnRvF")
# data = obj.generateSession('PNPT1158', '1598',pyotp.TOTP("FZ7F2L2AYUGDWPR4YBSSBYTU7Q").now())
# refreshToken= data['data']['refreshToken']


api_key = '3JhtnRvF'
username = 'PNPT1158'
pwd = '1598'
smartApi = SmartConnect(api_key = '3JhtnRvF')
try:
    token = "FZ7F2L2AYUGDWPR4YBSSBYTU7Q"
    totp = pyotp.TOTP(token).now()
except Exception as e:
    logger.error("Invalid Token: The provided token is not valid.")
    raise e

correlation_id = "abcde"
data = smartApi.generateSession(username, pwd, totp)

if data['status'] == False:
    logger.error(data)
else:
    # login api call
    # logger.info(f"You Credentials: {data}")
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']
    # fetch the feedtoken
    feedToken = smartApi.getfeedToken()
    # fetch User Profile
    res = smartApi.getProfile(refreshToken)
    smartApi.generateToken(refreshToken)
    res=res['data']['exchanges']

    
    # credentials.FEED_TOKEN = feedToken
    # print(feedToken)

#################Angle Brokering####################

def stockscreener():
    while True:
        try:
            with requests.session() as s:
                r_data = s.get(url)
                soup = bs(r_data.content,features="html.parser")
                meta = soup.find("meta", {"name" : "csrf-token"})["content"]

                header = {"x-csrf-token" : meta}
                data = s.post(url, headers=header, data=condition,).json()

                stock_list = pd.DataFrame(data["data"]).head(5)
                print("stock_list   ",stock_list)
                # print((stock_list["nsecode"].values.tolist()))
                act_lst= stock_list["nsecode"].values.tolist()

                # act_price = stock_list["close"].values.tolist()
        except Exception as E:
            print(f"Er first exception stock not found : {E}")


            def read_file_to_set(file_path):
                try:
                    with open(file_path, 'r') as file:
                        content = file.read().splitlines()
                        return set(content)
                except FileNotFoundError as FNFR:
                    logger.exception(f"FileNotFoundError: {FNFR}")
                    return set()

            def write_new_elements_to_file(file_path, new_elements, written_elements):
                try:
                    with open(file_path, 'a') as file:
                        for element in new_elements:
                            if element not in written_elements:
                                print("buy " ,element)
                                df = pd.read_csv("D:\codes\EQsymbol.csv")
                                
                                EQ_name = df.loc[df['symbol'] == element+"-EQ"]
                                EQ_name = (EQ_name["symbol"]).to_string(index=False)
                                print(EQ_name)
                                EQ_token = ((df.loc[df['symbol'] == element+"-EQ"]["token"]).to_string(index=False))
                                #place order
                                try:
                                    orderparams = {
                                            "variety": "NORMAL",
                                            "tradingsymbol": f"{EQ_name}",
                                            "symboltoken": f"{EQ_token}",
                                            "transactiontype": "BUY",
                                            "exchange": "NSE",
                                            "ordertype": "MARKET",
                                            "producttype": "DELIVERY",
                                            "duration": "DAY",
                                            # "price": close_p,
                                            "squareoff": "0",
                                            "stoploss": "0",
                                            "quantity": "1"}
                                    
                                    print(orderparams)
                                    # Method 1: Place an order and return the order ID
                                    # orderid = smartApi.placeOrder((orderparams))
                                    # logger.info(f"PlaceOrder : {orderid}")
                                    # Method 2: Place an order and return the full response
                                    # response = smartApi.placeOrderFullResponse((orderparams))
                                    # logger.info(f"PlaceOrder : {response}")
                                except Exception as e:
                                    logger.exception(f"Order placement failed: {e}")
                                file.write(element + '\n')
                                written_elements.add(element)
                except FileNotFoundError as FNFW:
                    logger.exception(f"FileNotFoundError: {FNFW,file_path}")
                    print(f"Error: File not found at {file_path}")
    
                def main():
                    os.path.join("D:\codes",name )
                    f = open(filename, "x")
                    f.close()
                    file_path = filename
                    # import os
                    # print(os)
                    written_elements = read_file_to_set(file_path)

                    while True:
                        try :
                        # Example: New elements to compare and potentially write to the file
                            new_elements = act_lst
                        # close_p = act_price

                            write_new_elements_to_file(filename, new_elements, written_elements)
                        except Exception as err:
                            pass
                        # print("New elements written to the file.")
                main()            
           
if __name__ == "__main__":

    stockscreener()


# package import statement


