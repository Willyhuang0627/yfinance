import yfinance as yf

def stock_info(id):
    tick = yf.Ticker(id)
    info = tick.info
    print(f'公司名稱 {info.get("shortName")}')
    print(f'最新訊息 {info.get("message")}')
    print(f'今日市場均價 {info.get("regularMarketPrice")}')
    print(f'今年度EPS {info.get("priceEpsCurrentYear")}')
    print(f'今日行情 {info.get("regularMarketDayRange")}')

def ticker_summary(id):
    tick = yf.Ticker(id)
    info = tick.fast_info
    print(f'開盤價{info.get("open")}')
    print(f'今日最高價{info.get("dayHigh")}')
    print(f'今日最低價{info.get("dayLow")}')
    print(f'目前價格{info.get("last_price")}')
    print(f'成交量{info.get("last_volume")}')     
          


#stock_info('2330.TW')
#stock_info('3533.TW')
print('------------台積電------------')
ticker_summary('2330.TW')
print('------------嘉澤------------')
ticker_summary('3533.TW')