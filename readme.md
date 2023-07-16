# Crypto Historical Data Fetcher

This script allows you to fetch historical cryptocurrency data from Binance. You can specify the symbol pair, the timeframe, and the start and end times to gather data. The data is saved as a JSON file.

If you use this script, please feel free to modify it and submit pull requests.

https://accounts.binance.com/register?ref=19776079

## Usage

```
git clone https://github.com/wishbid/BinanceCandlesticks.git
pip install ccxt arrow dateparser
```

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

Your output file will look similar to this
```json
{"timestamp": 1503187200000, "open": 4120.98, "high": 4211.08, "low": 4032.62, "close": 4086.29, "volume": 467.083022}
{"timestamp": 1503273600000, "open": 4069.13, "high": 4119.62, "low": 3911.79, "close": 4016.0, "volume": 691.74306}
{"timestamp": 1503360000000, "open": 4016.0, "high": 4104.82, "low": 3400.0, "close": 4040.0, "volume": 966.684858}
{"timestamp": 1503446400000, "open": 4040.0, "high": 4265.8, "low": 4013.89, "close": 4114.01, "volume": 1001.136565}
{"timestamp": 1503532800000, "open": 4147.0, "high": 4371.68, "low": 4085.01, "close": 4316.01, "volume": 787.418753}
{"timestamp": 1503619200000, "open": 4316.01, "high": 4453.91, "low": 4247.48, "close": 4280.68, "volume": 573.61274}
{"timestamp": 1503705600000, "open": 4280.71, "high": 4367.0, "low": 4212.41, "close": 4337.44, "volume": 228.108068}
{"timestamp": 1503792000000, "open": 4332.51, "high": 4400.0, "low": 4285.54, "close": 4310.01, "volume": 350.692585}
{"timestamp": 1503878400000, "open": 4310.01, "high": 4399.82, "low": 4124.54, "close": 4386.69, "volume": 603.841616}
{"timestamp": 1503964800000, "open": 4353.65, "high": 4625.85, "low": 4313.55, "close": 4587.48, "volume": 603.545028}
{"timestamp": 1504051200000, "open": 4564.52, "high": 4647.51, "low": 4416.01, "close": 4555.14, "volume": 808.468771}
```
