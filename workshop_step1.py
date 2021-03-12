import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import serial
import time
ser = serial.Serial('COM4')


ser.flushInput()

plot_window = 100
data = np.array(np.zeros([plot_window]))

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(data, color = 'purple', linewidth=2)


while True:
    try:
        ser_bytes = ser.readline()
        try:
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
        except:
            continue
        data = np.append(data,decoded_bytes)
        line.set_ydata(data[-plot_window:])
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()
    except:
        print("Keyboard Interrupt")
        break
