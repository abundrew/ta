# ------------------------------------------------------------------------------
# marubozu
# ------------------------------------------------------------------------------
def market_marubozu(market_ohlc, white = True):
    if white:
        m = [x for x in market_ohlc if
             x.open < x.close and x.open == x.low and x.close == x.high]
    else:
        m = [x for x in market_ohlc if
             x.open > x.close and x.open == x.high and x.close == x.low]
    return sorted(m, key = lambda x: abs(x.close - x.open) / x.high, reverse = True)

def market_opening_marubozu(market_ohlc, white = True):
    if white:
        m = [x for x in market_ohlc if
             x.open < x.close and x.open == x.low and x.close < x.high]
    else:
        m = [x for x in market_ohlc if
             x.open > x.close and x.open == x.high and x.close < x.low]
    return sorted(m, key = lambda x: abs(x.close - x.open) / x.high, reverse = True)

def market_closing_marubozu(market_ohlc, white = True):
    if white:
        m = [x for x in market_ohlc if
             x.open < x.close and x.open < x.low and x.close == x.high]
    else:
        m = [x for x in market_ohlc if
             x.open > x.close and x.open < x.high and x.close == x.low]
    return sorted(m, key = lambda x: abs(x.close - x.open) / x.high, reverse = True)
# ------------------------------------------------------------------------------
# doji
# ------------------------------------------------------------------------------
def market_dragonfly_doji(market_ohlc):
    m = [x for x in market_ohlc if
         x.open == x.close and x.open == x.high and x.open > x.low]
    return sorted(m, key = lambda x: abs(x.high - x.low) / x.high, reverse = True)
        
def market_gravestone_doji(market_ohlc):
    m = [x for x in market_ohlc if
         x.open == x.close and x.open == x.low and x.open < x.high]
    return sorted(m, key = lambda x: abs(x.high - x.low) / x.high, reverse = True)
# ------------------------------------------------------------------------------
