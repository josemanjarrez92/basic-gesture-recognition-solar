import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import serial
import ruptures as rpt
from scipy.signal import find_peaks

ser = serial.Serial('COM4')


ser.flushInput()

plot_window = 100
data = np.array(np.zeros([plot_window]))
obs_window = 20

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(data, color = 'purple', linewidth=2)
model="l2"

while True:
    try:
        ser_bytes = ser.readline()
        try:
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            #print(decoded_bytes)
        except:
            continue
        data = np.append(data,decoded_bytes*10)
        line.set_ydata(data[-plot_window:])

        ax.set_ylim(0,11)
        fig.canvas.draw()
        fig.canvas.flush_events()
        algo = rpt.Pelt(model=model).fit(data[-obs_window:])

        result1 = algo.predict(pen=0.9)
        if len(result1) > 2 :
            #print("Gesture Location: ", result1[:2])
            peaks,_ = find_peaks(data[-obs_window:], height = 1)

            if len(peaks) == 1:
                print("Gesture 1")
            elif len(peaks) == 2:
                print("Gesture 2")
    except:
        print("Keyboard Interrupt")
        break
