# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:39:45 2013

@author: cent
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# tick = np.load("tick.npy")

tick = pd.read_csv("rb.csv", encoding='gbk')

length = len(tick)

diff = np.append(0, np.diff(tick[u"收盘价"]))
position = np.zeros(length, np.int)
status = np.zeros(length, np.int)
p = 0
buyp = 0
sellp = 0
shijian = 0

for i in range(10, length):
    if tick["time"][i] > 9.15 and tick["time"][i] < 15.15:
        if tick["bidprice"][i] < tick["bidprice"][i - 1] and tick["bidvol"][i - 1] < 6 and tick["askvol"][
            i] < 6 and p != 1:
            position[i] = 1
            p = 1
            buyp = tick["bidprice"][i]
            shijian = 0
        if tick["askprice"][i] > tick["askprice"][i - 1] and tick["askvol"][i - 1] < 6 and tick["bidvol"][
            i] < 6 and p != -1:
            position[i] = -1
            p = -1
            sellp = tick["askprice"][i]
            shijian = 0
        if p == 1 and tick["bidprice"][i] > buyp + 2:
            position[i] = 0
            p = 0
        if p == -1 and tick["askprice"][i] < sellp - 2:
            position[i] = 0
            p = 0

    if tick["time"][i] > 15.14:
        position[i] = 0
        p = 0
        shijian = 0
    status[i] = p
    shijian = shijian + 1
price = tick['lastprice']
price[status > 0] = tick['bidprice'][status > 0]
price[status < 0] = tick['askprice'][status < 0]
dif = np.append(0, np.diff(price))
r = np.multiply(np.append(0, status[0:length - 1]), dif)
cr = np.cumsum(r)
cs = np.count_nonzero(position)
sy = cr[length - 2] * 300
abssy = cr[length - 1] * 300 - cs * 40
ykb = (cr[length - 1] * 300 - cs * 40) / (cs * 40)
plt.plot(cr)
plt.show()
