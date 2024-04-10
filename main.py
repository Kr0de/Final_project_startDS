import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

db = pd.read_excel('wage_2000_2023.xlsx').transpose().values
columns = db[0]
val = db[1:]
years = pd.read_excel('wage_2000_2023.xlsx').columns.values[1:]

fig, ax = plt.subplots(2, 2, figsize = (8, 6))
fig.tight_layout(h_pad = 5)

ax[0, 0].plot(years, val[:, 0] / 10 ** 3)
ax[0, 0].set_title(columns[0])
ax[0, 0].set_ylabel('тыс. руб.')
ax[0, 0].set_xlabel('Год')

ax[0, 1].plot(years, val[:, 1] / 10 ** 3)
ax[0, 1].set_title(columns[1])
ax[0, 1].set_ylabel('тыс. руб.')
ax[0, 1].set_xlabel('Год')

gs = ax[1, 1].get_gridspec()
for a in ax[1, :]:
    a.remove()

axbig = fig.add_subplot(gs[1, :])
axbig.plot(years, val[:, 2] / 10 ** 3)
axbig.set_title(columns[2])
axbig.set_ylabel('тыс. руб.')
axbig.set_xlabel('Год')

plt.subplots_adjust(top = 0.85, left = 0.15, bottom = 0.1)
plt.show()

#подключаем инфляцию
infl = pd.read_excel('level_inf.xlsx')
infl_year = infl['Год']
infl_total = infl['Всего'][::-1]


for i in range(3):
    fig, ax = plt.subplots(1, 2, figsize = (8, 6))
    fig.tight_layout(h_pad = 5)

    ax[0].plot(years, val[:, i] / 10 ** 3)
    ax[0].set_title(columns[i])
    ax[0].set_ylabel('тыс. руб.')
    ax[0].set_xlabel('Год')

    ax[1].plot(years, [a / (1 + b) for a, b in zip(val[:, i] / 10 ** 3, infl_total)])
    ax[1].set_title(f'{columns[i]} \n с учетом инфляции')
    ax[1].set_ylabel('тыс. руб.')
    ax[1].set_xlabel('Год')

    plt.subplots_adjust(top = 0.85, left = 0.15, bottom = 0.1)
    plt.show()



