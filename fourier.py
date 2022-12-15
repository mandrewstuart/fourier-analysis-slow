"Fourier analysis to decompose complex waves. It also generates a random wave for you"
import math
import plotly
from random import random


def main():
    # each pair is made of the frequency and amplitude.
    # note: because the only uncommented pair has frequency of 11,
    # the last browser tab will show the 10 as the highest magnitude (indicating 0-indexed)
    pairs = [[11, 10],
            #[51, 14]
             ]
    length = 600
    # define a series into a file
    create_defined_series(pairs, length)
    # read from the file
    series = get_series()
    # examine the series using plotly, which opens a browser
    plot = plotly.plot(series, kind='line', title='data to decompose')
    plot.show()
    # decompose the provided series in to sine, cosine, and sums
    slow_fourier_analysis(series)


def slow_fourier_analysis(series):
    sines = slow_fourier_helper(series, math.sin)
    plot = plotly.plot(sines, kind='line', title="sines")
    plot.show()
    coses = slow_fourier_helper(series, math.cos)
    plot = plotly.plot(coses, kind='line', title="coses")
    plot.show()
    sums = [coses[o]+sines[o] for o in range(len(series))]
    plot = plotly.plot(sums, kind='line', title="sums")
    plot.show()


def slow_fourier_helper(series, fn):
    num_elements = len(series)
    coefficients = []
    for period in range(num_elements):
        coefficient_total = 0
        for index in range(num_elements):
            amount = 2*math.pi*index/(1+period)
            coefficient_total += fn(amount)*series[index]
        coefficients.append(coefficient_total)
    coefficients = [c/(len(series)/2) for c in coefficients]
    return [0] + coefficients


def create_defined_series(pairs, num_elements):
    final_series = [1 for _ in range(num_elements)]
    for pair in pairs:
        for index in range(num_elements):
            amount = 2*math.pi*index/pair[0]
            tmp = pair[1] * math.sin(amount)
            final_series[index] = tmp * final_series[index]
    series_string = ",".join(str(f) for f in final_series)
    f = open("define_series.data", "w")
    f.write(series_string)
    f.close()


def create_series():
    series_length = 500
    series = ",".join([str(random()) for _ in range(series_length)])
    f = open("series.data", "w")
    f.write(series)
    f.close()


def get_series(whatever=False):
    if whatever:
        return [float(f) for f in open("series.data", "r").read().split(",")]
    else:
        return [float(f) for f in open("define_series.data", "r").read().split(",")]
    


if __name__ == '__main__':
    main()
