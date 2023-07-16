# Crypto Historical Data Fetcher

This script allows you to fetch historical cryptocurrency data from Binance. You can specify the symbol pair, the timeframe, and the start and end times to gather data. The data is saved as a JSON file.

If you use this script, please feel free to modify it and submit pull requests.

https://accounts.binance.com/register?ref=19776079

## Dependencies

Please install these before use.
- ccxt
- json
- arrow
- argparse
- dateparser

## Usage

```
python <script_name>.py -s <start_time> -e <end_time> -x <symbol> -t <timeframe>
```

### Arguments

- `-s`, `--start_time`: Start time of the range for which you want the historical data. You can use pretty much any format you want, e.g. ("YYYY.MM.DD", "YYYY.mm.dd HH:MM:SS")
- `-e`, `--end_time`: End time of the range for which you want the historical data.
- `-x`, `--symbol`: The trading symbol pair, e.g., "BTC/USDT", "ETH/USDT".
- `-t`, `--timeframe`: The timeframe for the data. Options are '1m', '3m', '5m', '15m', '30m', '1h', '4h', '8h', '12h', '1d', '1w', '1M'.
- `-f`, `--filename`: Filename for the output file. Default is 'historical_data'.
- `-r`, `--rate_limit`: Rate limit override. Default is 125 (No need to change its pretty fast).

### Example

```
python <script_name>.py -s "2023.01.01" -e "2023.07.16" -x "BTC/USDT" -t "1h"
```

This will fetch the historical OHLCV data for the BTC/USDT pair from 1st January 2023 to 16th July 2023 in 1-hour timeframes and save it to a file named 'btc_usdt_data.json'.
