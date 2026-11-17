# Crypto exchange listings and the price after them

Every new coin listing and delisting announced by 10 crypto exchanges, 2024-11-17 to 2026-11-17, with the price 5 minutes, 1 hour, 24 hours and 7 days later. 4,121 events, 2,390 of them with measured prices.

The data behind [newcoinlistings.com](https://newcoinlistings.com), where the same table is live and updated every minute: [what happens to the price after a listing, by exchange](https://newcoinlistings.com/listing-effect).

Exported 2026-11-17.

## What a listing usually does to the price

Median move after the event, groups with 10 or more measured listings:

| Exchange | Event | Counted from | Listings | 5 min | 1 h | 24 h | 7 days | Best within 1 h | Higher after 7 days |
|---|---|---|---|---|---|---|---|---|---|
| Binance | spot listing | announcement | 46 | +6.2% | +10.5% | +5.6% | -1.3% | +22.6% | 48% |
| Binance | spot listing | first trade | 14 | -1.6% | -0.5% | -24% | -28.9% | +4.1% | 36% |
| Upbit | spot listing | announcement | 152 | +17.9% | +18% | +8.3% | +2.5% | +34.4% | 57% |
| Upbit | spot listing | first trade | 26 | +0.1% | -4% | -16.6% | -38.4% | +4.9% | 8% |
| Bybit | spot listing | first trade | 37 | 0% | -4.2% | -13.1% | -29.8% | +16.6% | 30% |
| Bybit | spot listing | announcement | 29 | 0% | +0.2% | -4.4% | -16.8% | +3.1% | 36% |
| Coinbase | spot listing | start of trading | 77 | +0.1% | +1% | -0.4% | -8.2% | +2.4% | 33% |
| Coinbase | spot listing | first trade | 57 | -0.5% | -1% | -8.1% | -23.1% | +4.6% | 22% |
| OKX | spot listing | start of trading | 56 | 0% | -0.8% | -5.2% | -13.7% | +3.1% | 24% |
| OKX | spot listing | first trade | 28 | +1.2% | -3% | -8.1% | -27.9% | +13.3% | 21% |
| Gate | spot listing | first trade | 161 | -2.1% | -8.2% | -17.8% | -31.3% | +10.7% | 31% |
| Gate | spot listing | start of trading | 89 | 0% | -0.6% | -6.3% | -13.4% | +3.4% | 29% |
| HTX | spot listing | start of trading | 130 | 0% | 0% | -1.4% | -4.7% | +1.2% | 36% |
| HTX | spot listing | first trade | 40 | -0.5% | -2.3% | -14.8% | -40.9% | +13.4% | 23% |
| BingX | spot listing | start of trading | 115 | 0% | +0.1% | 0% | -2.8% | +1.6% | 42% |
| BingX | spot listing | first trade | 100 | -0.1% | -3.3% | -14.8% | -31.3% | +12.3% | 26% |
| MEXC | spot listing | first trade | 172 | -0.2% | -6.8% | -12.4% | -27.6% | +12% | 29% |
| MEXC | spot listing | start of trading | 74 | 0% | -0.2% | -4.1% | -12.5% | +3.5% | 24% |
| Binance | futures listing | announcement | 150 | +4.7% | +5% | +1.5% | -8.1% | +14.5% | 45% |
| Binance | futures listing | first trade | 42 | +0.1% | +0.3% | -8.9% | -16% | +6.2% | 36% |
| Bybit | futures listing | announcement | 309 | +0.4% | +0.9% | -2.8% | -14.6% | +5.7% | 32% |
| Bybit | futures listing | first trade | 45 | -1% | -0.2% | -6.4% | -18.1% | +5.8% | 36% |
| Binance | delisting | announcement | 112 | -11.2% | -16% | -22.2% | -36.1% | +0.1% | 8% |
| Upbit | delisting | announcement | 26 | -6.2% | -5.6% | -8% | -11.2% | +0.2% | 9% |
| Bybit | delisting | announcement | 237 | -0.8% | -0.8% | -2.2% | -6.9% | +0.4% | 27% |
| Upbit | warning | announcement | 50 | -1% | -3% | -6.4% | -11.2% | +1.3% | 22% |

The same numbers as a file: `listing-effect.csv`.

## Files

- `listings.csv`: one row per event. BingX 909, Bybit 663, MEXC 641, Gate 600, Binance 389, HTX 328, Upbit 291, Coinbase 184, OKX 101, KuCoin 15. By kind: spot 3084, futures 567, warning 67, delist 403.
- `listing-effect.csv`: the medians above, every group.

```python
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/pianist161/crypto-exchange-listings/main/listings.csv", parse_dates=["announced_at", "trade_at", "start_at"])
upbit = df[(df.exchange == "upbit") & (df.kind == "spot") & (df.counted_from == "announcement")]
print(upbit.change_5m_pct.median(), upbit.change_7d_pct.median())
```

The table above recomputed from `listings.csv` with nothing but Python's standard library: `python examples/listing_effect.py` ([source](examples/listing_effect.py)). Its output matches `listing-effect.csv`.

## Columns of listings.csv

| Column | Meaning |
|---|---|
| `id` | Our id of the event. |
| `exchange` | bingx, bybit, mexc, gate, binance, htx, upbit, coinbase, okx, kucoin. |
| `ticker` | The coin's ticker on that exchange. |
| `kind` | `spot` (spot listing), `futures` (perpetual futures listing), `delist` (delisting), `warning` (Upbit's caution notice). |
| `market`, `title`, `announcement_url` | The pair or market, the exchange's own title and the address of its announcement. |
| `announced_at` | When the exchange announced it, UTC. For exchanges read by their list of markets (OKX, Gate, HTX, BingX, MEXC, Coinbase's past listings) it is when trading opened. |
| `trade_at` | When trading opens (a delisting: ends), where the exchange said so. |
| `counted_from` | Where the price is counted from: `announcement`; `start of trading` (the coin already traded elsewhere: 10 minutes before trading opened on this exchange); `first trade` (the coin was new to the market: 5 minutes after its first trade). Empty: no market to measure on. Never mix the three in one average. |
| `start_at`, `price_venue`, `start_price` | The moment and the market the start price was read at (public 1-minute candles) and the price. Prices are in the quote currency of that market: dollars or USDT, won for `upbit:KRW-…`. |
| `price_5m` … `price_7d`, `peak_price_1h` | The price that long after `start_at`, and the highest price within the first hour. Empty while not yet reached. |
| `change_5m_pct` … `change_7d_pct`, `peak_1h_pct` | The same as a change from `start_price`, in percent. |
| `page` | The coin's page with its chart and every listing of it. |

## How it is collected

- Binance, Upbit, Bybit, KuCoin: the exchanges' own announcement feeds, read every minute. An event is counted from the minute of the announcement.
- Coinbase, OKX, Gate, HTX, BingX, MEXC, Kraken, Crypto.com, Bithumb: their public lists of markets. A pair never seen before is a listing; where the list carries the time trading opened, past listings are taken from it.
- Prices: public 1-minute candles of Binance, Bybit, KuCoin, Coinbase, Gate, MEXC and Upbit.
- Left out: tokens of stocks and funds, leveraged tokens, indexes, perpetual contracts on shares and commodities.
- Method in full: [newcoinlistings.com/about](https://newcoinlistings.com/about).

Live, without this repository: the latest 500 events as JSON at `https://newcoinlistings.com/raw/events.json`, RSS at `https://newcoinlistings.com/feed.xml`. The same files on Kaggle: [kaggle.com/datasets/newlisting/crypto-exchange-listings-and-price-after-listing](https://www.kaggle.com/datasets/newlisting/crypto-exchange-listings-and-price-after-listing).

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): use it for anything, with a link to [newcoinlistings.com](https://newcoinlistings.com) as the source. Not financial advice.
