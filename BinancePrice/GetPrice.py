
#------ librarys's--------
import nest_asyncio
import websockets
import asyncio
import json
import pandas as pd
import redis

nest_asyncio.apply()

#------ list of coins
coins = ["btcusdt", "ethusdt", "ltcusdt", "linkusdt",
 "xlmusdt", "uniusdt", "filusdt"]
 
coins_price= []
for coin in coins:
    async def main():
        #binance API address
        socket = f"wss://stream.binance.com:9443/ws/{coin}@depth@100ms"
        async with websockets.connect(socket, timeout = 60 ) as ws:
            #return price of the asset
            return await ws.recv()

    if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        receive_message = loop.run_until_complete(asyncio.gather(main()))
        #reading received message
        try:
            obj = json.loads(receive_message[0])
            price =  obj['a'][0][0]
        except:
            obj = json.loads(receive_message[0])
            price =  obj['b'][0][0]
            
        print(coin,price)
        #storing values on dic
        
        coins_price.append(round(float(price),2))
        
        
#-------------creating dataframe with values--------------
dic = {'COIN': coins, "PRICE ($)": coins_price}
df = pd.DataFrame(dic)
print(df)
