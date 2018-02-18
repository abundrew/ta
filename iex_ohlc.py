from collections import namedtuple
import iex_api

TOhlc = namedtuple('TOhlc', ['symbol', 'open', 'high', 'low', 'close'])

def market_ohlc():
    data = iex_api.stock_batch_100('ohlc')
    if data['success']:
        result = []
        for k, v in data['data'].items():
            if ('ohlc' in v and
                'close' in v['ohlc'] and 'price' in v['ohlc']['close'] and
                'open' in v['ohlc'] and 'price' in v['ohlc']['open'] and
                'high' in v['ohlc'] and 'low' in v['ohlc']):
                result.append(TOhlc(k,
                                    v['ohlc']['open']['price'],
                                    v['ohlc']['high'],
                                    v['ohlc']['low'],
                                    v['ohlc']['close']['price']))
        return result
    else:
        return []
