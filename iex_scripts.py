script = 2

if script == 0:
    #---------------------------------------------------------------------------
    # white marubozu symbols
    #---------------------------------------------------------------------------
    import iex_ohlc
    import iex_patterns
    
    ohlc = iex_ohlc.market_ohlc()
    marubozu = iex_patterns.market_marubozu(ohlc)
    print('-' * 30)
    print('white marubozu symbols:')
    print('-' * 30)
    print(','.join((x.symbol for x in marubozu)))
    print('-' * 30)

elif script == 1:
    #---------------------------------------------------------------------------
    # open chart in browser for symbol
    #---------------------------------------------------------------------------
    import webbrowser

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    symbol = 'UAN'
    url = 'https://www.tradingview.com/chart/?symbol={}'.format(symbol)
    webbrowser.get(chrome_path).open(url)

elif script == 2:
    #---------------------------------------------------------------------------
    # charts for 20 white maribozu symbols
    #---------------------------------------------------------------------------
    import iex_ohlc
    import iex_patterns
    
    ohlc = iex_ohlc.market_ohlc()
    marubozu = iex_patterns.market_marubozu(ohlc)
    
    import webbrowser
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    
    for item in marubozu[:20]:
        url = 'https://www.tradingview.com/chart/?symbol={}'.format(item.symbol)
        webbrowser.get(chrome_path).open(url)

elif script == 3:
    #---------------------------------------------------------------------------
    # dragonfly doji symbols
    #---------------------------------------------------------------------------
    import iex_ohlc
    import iex_patterns
    
    ohlc = iex_ohlc.market_ohlc()
    doji = iex_patterns.market_dragonfly_doji(ohlc)
    print('-' * 30)
    print('dragonfly doji symbols:')
    print('-' * 30)
    print(','.join((x.symbol for x in doji)))
    print('-' * 30)

elif script == 4:
    #---------------------------------------------------------------------------
    # charts for 20 dragonfly doji symbols
    #---------------------------------------------------------------------------
    import iex_ohlc
    import iex_patterns
    
    ohlc = iex_ohlc.market_ohlc()
    doji = iex_patterns.market_dragonfly_doji(ohlc)
    
    import webbrowser
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    
    for item in doji[:20]:
        url = 'https://www.tradingview.com/chart/?symbol={}'.format(item.symbol)
        webbrowser.get(chrome_path).open(url)

