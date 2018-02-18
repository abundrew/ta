import webbrowser

import iex_ohlc
import iex_patterns

CHROME_PATH = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
CHART_URL = 'https://www.tradingview.com/chart/?symbol={}'

def get_ohlc():
    if get_ohlc.ohlc == None:
        print('loading...')
        get_ohlc.ohlc = iex_ohlc.market_ohlc()
    return get_ohlc.ohlc
get_ohlc.ohlc = None

while True:
    print('=' * 40)
    print('iex scripts')
    print('-' * 40)
    print('1 - symbol chart')
    print('2 - white marubozu symbols')
    print('3 - dragonfly doji symbols')
    print('0 - exit')
    print('=' * 40)
    print('enter script #', end=':')
    script = int(input())

    if script == 0: break

    if script == 1:
        #---------------------------------------------------------------------------
        # symbol chart
        #---------------------------------------------------------------------------
        print('enter symbol', end=':')
        symbol = input()
        url = CHART_URL.format(symbol)
        webbrowser.get(CHROME_PATH).open(url)

    elif script == 2:
        #---------------------------------------------------------------------------
        # white marubozu symbols
        #---------------------------------------------------------------------------
        marubozu = iex_patterns.market_marubozu(get_ohlc())
        print('-' * 40)
        print('white marubozu symbols [{}]:'.format(len(marubozu)))
        print('-' * 40)
        print(','.join((x.symbol for x in marubozu)))
        print('-' * 40)

        print('enter number of charts', end=':')
        n_charts = int(input())
        for item in marubozu[:n_charts]:
            url = CHART_URL.format(item.symbol)
            webbrowser.get(CHROME_PATH).open(url)

    elif script == 3:
        #---------------------------------------------------------------------------
        # dragonfly doji symbols
        #---------------------------------------------------------------------------
        doji = iex_patterns.market_dragonfly_doji(get_ohlc())
        print('-' * 40)
        print('dragonfly doji symbols [{}]:'.format(len(doji)))
        print('-' * 40)
        print(','.join((x.symbol for x in doji)))
        print('-' * 40)

        print('enter number of charts', end=':')
        n_charts = int(input())
        for item in doji[:n_charts]:
            url = CHART_URL.format(item.symbol)
            webbrowser.get(CHROME_PATH).open(url)
