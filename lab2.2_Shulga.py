# Шульга Є.К., ІО-71, № заліковки: 7130
# #  n w    N
# 30 14 2000 256

# Додаткове завдання: порівняйте час виконання fft вашої реалізації та numpy fft

import random as r
import math
import matplotlib.pyplot as plt
import numpy
import datetime

n = 14
w_max = 2000
N = 256


def graph(N):
    x = [0] * N

    for i in range(n):
        A = r.randrange(2)
        W = r.randrange(w_max)
        f = r.randrange(1e9)
        for t in range(N):
            x[t] += A * math.sin(W * t + f)
    return x


def fft(x: list):
    N = len(x)
    fftt = [[0] * 2 for i in range(N)]
    for i in range(N // 2):
        array1 = [0] * 2
        array2 = [0] * 2
        for j in range(N // 2):
            cos = math.cos(4 * math.pi * i * j / N)
            sin = math.sin(4 * math.pi * i * j / N)
            array1[0] += x[2 * j + 1] * cos # real
            array1[1] += x[2 * j + 1] * sin # imag
            array2[0] += x[2 * j] * cos # real
            array2[1] += x[2 * j] * sin # imag
        cos = math.cos(2 * math.pi * i / N)
        sin = math.sin(2 * math.pi * i / N)
        fftt[i][0] = array2[0] + array1[0] * cos - array1[1] * sin # real
        fftt[i][1] = array2[1] + array1[0] * sin + array1[1] * cos # imag
        fftt[i + N // 2][0] = array2[0] - (array1[0] * cos - array1[1] * sin) # real
        fftt[i + N // 2][1] = array2[1] - (array1[0] * sin + array1[1] * cos) # imag
    return fftt


for x_size in range(256, 2560, 32):
    now = datetime.datetime.now()
    numpy.fft.fft(graph(x_size))
    np_time = datetime.datetime.now() - now

    now = datetime.datetime.now()
    fft(graph(x_size))
    fft_time = datetime.datetime.now() - now

    print('X size:', x_size, 'hand-written FFT time:', fft_time, ', Numpy fft time:', np_time)

exit(0)

X = graph(N)
fftt = fft(X)

data_fft = [math.sqrt(fftt[i][0] ** 2 + fftt[i][1] ** 2) for i in range(N)]

plt.plot([i for i in range(N)], X)
plt.show()
plt.plot([i for i in range(N)], data_fft)
plt.show()
