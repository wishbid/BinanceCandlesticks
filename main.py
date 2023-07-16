import ccxt
import json
import arrow
import argparse
import dateparser


def main():
    timeframes_set = {'1m', '3m', '5m', '15m', '30m', '1h', '4h', '8h', '12h', '1d', '1w', '1M'}

    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--start_time', required=True, type=str,
                        help='use whatever format you want, ("YYYY.MM.DD", "YYYY.mm.dd:HH:MM:SS")')
    parser.add_argument('-e', '--end_time', required=True)
    parser.add_argument('-x', '--symbol', required=True,
                        help='trading symbol, etc [BTC/USDT, ETH/USDT]')
    parser.add_argument('-t', '--timeframe', default='1m', choices=timeframes_set,
                        help='candlesticks timeframe')
    parser.add_argument('-f', '--filename', default='historical_data',
                        help='file name to save file')
    parser.add_argument('-r', '--rate_limit', default=125, const=True, type=int, nargs='?',
                        help='rate limit override, you probably dont need to touch this')
    args = parser.parse_args()

    exchange = ccxt.binance({
        'rateLimit': 125,  # adjust to avoid hitting rate limits
        'enableRateLimit': True,
    })

    symbol = args.symbol
    timeframe = args.timeframe
    start = dateparser.parse(args.start_time)
    end = dateparser.parse(args.end_time)

    since = int(start.timestamp()) * 1000
    end = int(end.timestamp()) * 1000

    print(f'Running for pair({symbol}), timeframe({timeframe})')
    print(f'Start: \t{arrow.get(start)}')
    print(f'End: \t{arrow.get(end)}')

    data = []
    # Loop over the time range and fetch OHLCV data
    while since < end:
        try:
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since, limit=1500)
            print(f'Last time received {arrow.get(ohlcv[-1][0])}')
            if len(ohlcv) == 0:
                print(f'Message received for {arrow.get(ohlcv[-1][0])} is empty')
                break
            data.extend(ohlcv)
            since = ohlcv[-1][0] + 1  # get start timestamp of next minute
        except Exception as e:
            print(f'Fetch failed: {e}')
            break

    # Convert to JSON and save to file
    with open(args.filename + '.json', 'w') as f:
        for line in data:

            # Sometimes we grab more data than we need from the exchange. Break early if thats the case.
            if line[0] >= end:
                break

            f.write(json.dumps(
                {'timestamp': line[0], 'open': line[1], 'high': line[2], 'low': line[3], 'close': line[4],
                 'volume': line[5]}) + "\n")


if __name__ == "__main__":
    main()
