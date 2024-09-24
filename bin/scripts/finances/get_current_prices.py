import pandas
from pandas_datareader import data as pdr
from datetime import datetime, timedelta
import yfinance as yfin

def get_current_prices(symbols: list[str], padding=2):
  yfin.pdr_override()

  def fmt(date: datetime) -> str:
    return date.strftime('%Y-%m-%d')

  def get_close(symbol: str) -> float or None:
    try:
      today = datetime.today()
      temporal_padding = today - timedelta(padding)

      df = pdr.get_data_yahoo(symbol,
                  start=fmt(temporal_padding), end=fmt(today))
      return df.iloc[-1, 3]
    except:
      return None

  close_values = list(map(get_close, symbols))

  current_prices = { symbol[:-4]: { 'price': close }\
                    for symbol, close in zip(symbols, close_values) if close }

  return current_prices

# Example
# df = pd.DataFrame(get_current_prices(['BTC-USD', 'ETH-USD', 'USDC-USD']))