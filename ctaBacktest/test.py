# -*- coding:utf-8 -*-


import pandas as pd

df = pd.read_csv("rb.csv", encoding='gbk')

print df.head()

h = df.head()


def MA(self, price, windows=5, period=1):
    MAprice = pd.rolling_mean(price, windows, period)
    return MAprice


def gen_signal(self):
    signals = pd.DataFrame(index=self.bars.index)
    signals['flag'] = 0
    signals['sma'] = self.MA(self.bars['close'], self.short_window, 1)
    signals['lma'] = self.MA(self.bars['close'], self.long_window, 1)
    signals['flag'][self.short_window:] = np.where(
        signals['sma'][self.short_window:] > signals['lma'][self.short_window:], 1, 0)
    signals['signal'] = signals['flag'].diff().fillna(signals['flag'][0])
    return signals


def gen_positions(self):
    positions = self.signals['flag'] * 1000
    return positions


def trade_positions(self):
    positions = self.signals['signal'] * 1000
    return positions


def trade_tracing(self):
    capital = pd.DataFrame(index=self.signals.index)
    capital['hold'] = self.gen_positions() * self.bars['close']
    capital['rest'] = self.init_capital - (self.trade_positions() * bars['close']).cumsum()
    capital['total'] = capital['hold'] + capital['rest']
    capital['return'] = capital['total'].pct_change().fillna(capital['total'][0] / self.init_capital - 1)
    return capital
