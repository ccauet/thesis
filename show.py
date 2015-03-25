#!/usr/bin/env python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime
# import pytz
# from pytz import timezone

if __name__ == "__main__":
  data = np.genfromtxt('/Users/ccauet/Repositories/thesis/wordcount.txt', dtype=None)

  # print data

  # for timestamp, wordcount in data:
  #   dt = datetime.datetime.strptime(timestamp[:-13], '%Y-%m-%dT%H:%M:%S')
  #   print dt, wordcount

  years = YearLocator()   # every year
  months = MonthLocator()  # every month
  yearsFmt = DateFormatter('%Y')

  dates = [datetime.datetime.strptime(timestamp[0][:-13], '%Y-%m-%dT%H:%M:%S') for timestamp in data]
  words = [q[1] for q in data]

  print dates, words

  fig, ax = plt.subplots()
  ax.plot_date(dates, words, '-')

  # # format the ticks
  # ax.xaxis.set_major_locator(years)
  # ax.xaxis.set_major_formatter(yearsFmt)
  # ax.xaxis.set_minor_locator(months)
  # ax.autoscale_view()

  # ax.fmt_xdata = DateFormatter('%Y-%m-%dT%H:%M:%S')
  # ax.fmt_ydata = price
  # ax.grid(True)

  fig.autofmt_xdate()
  plt.show()